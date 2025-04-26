from user_auth.models.base_user_model.user import *
from user_auth.models.student_package.model_courses import *


class Student(BaseModel):
    STATUS_CHOICES = [
        ('active', 'Учится сейчас'),
        ('end', 'Закончил обучение'),
        ('left', 'Не закончил и ушёл'),
    ]

    surname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ManyToManyField('Group', blank=True, related_name='students_in_group')
    courses = models.ManyToManyField('Course', blank=True, related_name='students_in_course')
    is_line = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    student_position = models.CharField(max_length=15,choices=STATUS_CHOICES,default='active',null=True,blank=True)

    def __str__(self):
        return f"{self.surname}, {self.firstname}, {self.lastname}"



class Parents(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    descriptions = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.phone_number})"
