from user_auth.models import BaseModel
from django.db import models
from dateutil.relativedelta import relativedelta
from math import ceil
from dateutil.relativedelta import relativedelta
#+
# дни учебы
class StudyDay(models.Model):
    Course_Days = [
        ('mon', 'Понедельник'),
        ('tue', 'Вторник'),
        ('wed', 'Среда'),
        ('thu', 'Четверг'),
        ('fri', 'Пятница'),
        ('sat', 'Суббота'),
        ('sun', 'Воскресенье'),
    ]
    code = models.CharField(max_length=3, choices=Course_Days, unique=True)
    title = models.CharField(max_length=20)

    def __str__(self):
        return dict(self.Course_Days).get(self.code, self.title)

#+
# продолжительность курса
class CourseDuration(BaseModel):
    course_start_time = models.DateField()
    course_end_time = models.DateField()
    work_days = models.ManyToManyField('StudyDay', related_name='course_durations')
    total_duration = models.IntegerField(editable=False, null=True)  # Добавление поля для продолжительности курса

    def save(self, *args, **kwargs):
        # Вычисляем продолжительность курса
        delta = relativedelta(self.course_end_time, self.course_start_time)
        months = delta.years * 12 + delta.months
        if delta.days > 0:
            months += 1  # Учитываем частичный месяц
        self.total_duration = months  # Заполняем поле total_duration
        super().save(*args, **kwargs)

    def __str__(self):
        return f" недель ({self.total_duration} мес.) с {self.course_start_time} по {self.course_end_time}"

#+

# левел курса начинающий или уже продвинутый
class CourseLevel(BaseModel):
    COURSE_LEVELS = [
        ('beg', 'Базовый'),
        ('mid', 'Средний'),
        ('adv', 'Продвинутый'),
    ]
    course_level = models.CharField(max_length=3, choices=COURSE_LEVELS, default='beg')

    def __str__(self):
        return f"{self.course_level}"

#+
# курс
class Course(BaseModel):
    course_cost_per_week = models.IntegerField()
    course_total_cost = models.IntegerField(editable=False)
    course_name = models.CharField(max_length=90)
    course_descriptions = models.TextField(max_length=150)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    mentor = models.ForeignKey('Mentor', on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')

    course_level = models.ForeignKey(CourseLevel, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')

    course_duration = models.OneToOneField(CourseDuration, on_delete=models.CASCADE, related_name='course')

    def save(self, *args, **kwargs):
        # Используем поле total_duration из модели CourseDuration для расчета стоимости курса
        if self.course_duration:
            self.course_total_cost = self.course_cost_per_week * self.course_duration.total_duration
        super().save(*args, **kwargs)

    def __str__(self):
        return self.course_name

