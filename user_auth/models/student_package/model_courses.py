from user_auth.models import BaseModel
from django.db import models


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
        return self.title

class CourseDuration(BaseModel):
    total_duration = models.IntegerField()
    course_start_time = models.DateField()
    course_end_time = models.DateField()
    work_days = models.ManyToManyField(StudyDay, related_name='course_durations')

    def __str__(self):
        return f"{self.total_duration} недель с {self.course_start_time} по {self.course_end_time}"

class CourseLevel(BaseModel):
    COURSE_LEVELS = [
        ('beg', 'Базовый'),
        ('mid', 'Средний'),
        ('adv', 'Продвинутый'),
    ]
    course_level = models.CharField(max_length=3, choices=COURSE_LEVELS, default='beg')

    def __str__(self):
        return f"{self.course_level}"

class Course(BaseModel):
    course_cost_per_week = models.IntegerField()
    course_total_cost = models.IntegerField(editable=False)
    course_name = models.CharField(max_length=90)
    course_descriptions = models.TextField(max_length=150)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    mentor = models.ForeignKey('Mentor', on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')

    course_level = models.ForeignKey(CourseLevel, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')  # <-- вот тут добавили связь

    course_duration = models.OneToOneField(CourseDuration, on_delete=models.CASCADE, related_name='course')

    def save(self, *args, **kwargs):
        if self.course_duration:
            self.course_total_cost = self.course_cost_per_week * self.course_duration.total_duration
        super().save(*args, **kwargs)

    def __str__(self):
        return self.course_name



# class Course(BaseModel):
#     course_cost_per_week = models.IntegerField()
#     course_total_cost = models.IntegerField(editable=False)
#     course_name = models.CharField(max_length=90)
#     course_descriptions = models.TextField(max_length=150)
#     teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, related_name='courses')
#     mentor = models.ForeignKey('Mentor', on_delete=models.SET_NULL, null=True, related_name='courses')
#
#
#     course_duration = models.OneToOneField(CourseDuration, on_delete=models.CASCADE, related_name='course')
#
#     def save(self, *args, **kwargs):
#         if self.course_duration:
#             self.course_total_cost = self.course_cost_per_week * self.course_duration.total_duration
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.course_name
