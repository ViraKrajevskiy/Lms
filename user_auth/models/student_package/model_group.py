from django.db import models
import datetime
from user_auth.models import BaseModel

# класс группа
class Group(BaseModel):
    title = models.CharField(max_length=50, unique=True)
    course = models.OneToOneField('Course', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, related_name='groups')
    mentor = models.ForeignKey('Mentor', on_delete=models.SET_NULL, null=True, related_name='groups')
    start_time = models.TimeField(default=datetime.time(9, 0))  # Значение по умолчанию
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title