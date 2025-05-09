from user_auth.models import BaseModel
from user_auth.models.student_package.model_group import Group
from user_auth.models.workers_models.model_worker import *

#+
# модель учителя и ментора
class Teacher(BaseModel):
    staff = models.OneToOneField('Staff', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.staff},"

#+
class Mentor(BaseModel):
    staff = models.OneToOneField('Staff', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.staff},"