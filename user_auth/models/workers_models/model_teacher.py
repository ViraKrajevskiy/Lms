from user_auth.models import BaseModel
from user_auth.models.student_package.model_group import Group
from user_auth.models.workers_models.model_worker import *

# модель учителя и ментора
class Teacher(BaseModel):
    staff = models.OneToOneField('Staff', on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    # teacher_group = models.ManyToManyField(Group, related_name='teachers')

    def __str__(self):
        return f"{self.staff},{self.user}"

class Mentor(BaseModel):
    staff = models.OneToOneField('Staff', on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    # mentor_group = models.ManyToManyField(Group, related_name='mentors')

    def __str__(self):
        return f"{self.staff}, {self.user}"