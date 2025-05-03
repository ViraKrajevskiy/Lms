from django.db import models
from django.db.models import JSONField
from django.utils import timezone
from user_auth.models.student_package.model_group import Group

# прищел или не прищел ученик
class Attendance(models.Model):
    STATUS_CHOICES = [
        ('absent', 'Не пришел'),
        ('present', 'Присутствовал'),
        ('late', 'Опоздал'),
    ]

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name='Группа'
    )
    date = models.DateField(
        default=timezone.now,
        verbose_name='Дата занятия'
    )
    students_status = JSONField(
        verbose_name='Статусы студентов',
        default=dict,
        help_text='Формат: {"student_id": "status"}'
    )

    # /
    class Meta:
        unique_together = ['group', 'date']
        ordering = ['-date']

    def __str__(self):
        return f"Посещение {self.group} - {self.date}"

    # status студента 
    def set_student_status(self, student_id, status):
        self.students_status[str(student_id)] = status
        self.save()

    def get_student_status(self, student_id):
        return self.students_status.get(str(student_id), 'absent')

    def get_all_present(self):
        return [
            int(student_id) for student_id, status
            in self.students_status.items()
            if status in ['present', 'late']
        ]

    @property
    def absent_students(self):
        return self.group.students.exclude(
            id__in=self.get_all_present()
        )

    def save(self, *args, **kwargs):
        # Автоматическое создание пустых статусов для новых студентов
        if self.pk:
            current_students = set(self.group.students.values_list('id', flat=True))
            existing_statuses = set(map(int, self.students_status.keys()))

            # Добавляем отсутствующих студентов
            for student_id in current_students - existing_statuses:
                self.students_status[str(student_id)] = 'absent'

            # Удаляем ушедших студентов
            for student_id in existing_statuses - current_students:
                del self.students_status[str(student_id)]

        super().save(*args, **kwargs)
