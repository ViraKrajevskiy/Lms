from user_auth.models import BaseModel
from django.db import models


class Group(BaseModel):
    title = models.CharField(max_length=50, unique=True)
    course = models.OneToOneField('Course', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, related_name='groups')
    mentor = models.ForeignKey('Mentor', on_delete=models.SET_NULL, null=True, related_name='groups')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descriptions = models.CharField(max_length=500, blank=True, null=True)
    students = models.ManyToManyField('Student', related_name='groups', blank=True)  # Здесь оставляем groups


    def __str__(self):
        return self.title
