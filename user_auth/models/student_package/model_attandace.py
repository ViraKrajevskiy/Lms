from django.db import models
from user_auth.models.Hw_model.model_lesson import Lesson
from user_auth.models.student_package.model_group import Group
from user_auth.models.student_package.model_student import Student

#Привязка класса к атандансе рекорд и также подвязка группы невозможность использование филда маний то маний

class Attendance(models.Model):
    date = models.DateField()
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='attendances')
    students = models.ManyToManyField('Student', through='AttendanceRecord', related_name='attendances')

    def save(self, *args, **kwargs):
        # Переопределяем save, чтобы автоматически добавить статус 'A' для студентов,

        # которые не были отмечены в AttendanceRecord
        super().save(*args, **kwargs)

        all_students = self.group.students.all()  # Получаем всех студентов группы
        existing_students = self.students.all()  # Получаем студентов, которые уже отмечены в AttendanceRecord

        # Студенты, которые не были отмечены, автоматически становятся "Отсутствуют"
        for student in all_students:
            if student not in existing_students:
                AttendanceRecord.objects.update_or_create(
                    attendance=self,
                    student=student,
                    defaults={'status': 'A'}  # Статус "Отсутствует"
                )

    def __str__(self):
        return f"Посещаемость {self.date} ({self.group})"


class AttendanceRecord(models.Model):
    ATTENDANCE_STATUS_CHOICES = [
        ('P', 'Пришел'),
        ('A', 'Отсутствует'),
        ('L', 'Опоздал'),
        ('E', 'Уважительная причина'),
    ]

    attendance = models.ForeignKey('Attendance', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=ATTENDANCE_STATUS_CHOICES)

    class Meta:
        unique_together = ('attendance', 'student')

    def __str__(self):
        return f"{self.student} - {self.attendance.date} - {self.get_status_display()}"

#кароче те кто опоздал по дефолту будут не будет не пришли