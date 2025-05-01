from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from user_auth.models import BaseModel

# Валидаторы файлов
def validate_video_size(file):
    #Проверка размера видео (макс. 200 МБ)
    max_size_mb = 200
    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Максимальный размер видео — {max_size_mb} МБ")

def validate_file_size(file):
    #Проверка размера файла (макс. 200 МБ)
    max_size_mb = 200
    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла — {max_size_mb} МБ")

# Домашнее задание для группы
class GroupHomework(BaseModel):
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='group_homeworks')
    title = models.CharField(max_length=255)
    video_lesson = models.FileField(
        upload_to='video_lessons/',
        validators=[validate_video_size],
        null=True,
        blank=True
    )
    description = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return f"{self.title} (Группа: {self.group.title})"

# Домашняя работа студента
class StudentHomework(BaseModel):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='student_homeworks')
    group_homework = models.ForeignKey('GroupHomework', on_delete=models.CASCADE, related_name='student_homeworks')
    file = models.FileField(
        upload_to='homeworks/',
        validators=[validate_file_size],
        blank=True,
        null=True
    )
    is_checked = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Проверка дедлайна
        if self.pk and self.group_homework.deadline < timezone.now():
            raise ValidationError("Срок сдачи истек. Изменения запрещены.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.surname} - {self.group_homework.title}"

# Дополнительные файлы к домашней работе
class StudentAddHw(BaseModel):
    homework = models.ForeignKey(
        'StudentHomework',
        on_delete=models.CASCADE,
        related_name='additional_files'
    )
    file = models.FileField(
        upload_to='homeworks/additional/',
        validators=[validate_file_size]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Проверка дедлайна и лимита файлов
        if self.homework.group_homework.deadline < timezone.now():
            raise ValidationError("Дедлайн прошел. Добавление файлов невозможно")
        if not self.pk and self.homework.additional_files.count() >= 5:
            raise ValidationError("Можно прикрепить не более 5 дополнительных файлов")

    def __str__(self):
        return f"Доп. файл к ДЗ #{self.homework.id}"