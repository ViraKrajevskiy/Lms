from django.db.models import CharField

from user_auth.models import BaseModel
from django.db import models

from user_auth.models.student_package.model_attandace import *


class Room(BaseModel):
    rom_name = CharField(max_length=90,default='Standard_room')
    rom_number = models.IntegerField()

class Lesson(BaseModel):
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    mentor = models.ForeignKey('Mentor', on_delete=models.SET_NULL, null=True, blank=True)
    lesson_topik = models.CharField(max_length=100)
    lesson_description = models.TextField(max_length=150)
    group_data = models.OneToOneField('GroupHomework',on_delete=models.CASCADE,related_name='group_and_hw')
    rom_numb = models.ForeignKey('Room',on_delete=models.SET_NULL,blank=True, null=True)
    attendance = models.ManyToManyField('Attendance',blank=True,related_name='Attendance')