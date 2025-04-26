from django.utils import timezone
from user_auth.models.base_user_model.user import BaseModel
from user_auth.models.student_package.model_courses import *

class WorkDay(BaseModel):
    DAYS_OF_WEEK = [
        ('mon', 'Понедельник'),
        ('tue', 'Вторник'),
        ('wed', 'Среда'),
        ('thu', 'Четверг'),
        ('fri', 'Пятница'),
        ('sat', 'Суббота'),
        ('sun', 'Воскресенье'),
    ]

    code = models.CharField(max_length=3, choices=DAYS_OF_WEEK, unique=True)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class WorkerAttendance(BaseModel):
    ATTENDANCE_STATUS_CHOICES_WORKER = [
        ('P', 'Пришел'),
        ('A', 'Отсутствует'),
        ('L', 'Опоздал'),
        ('E', 'Уважительная причина'),
    ]

    staff = models.ForeignKey('Staff', on_delete=models.CASCADE, related_name='attendances')
    work_day = models.ForeignKey(WorkDay, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=1, choices=ATTENDANCE_STATUS_CHOICES_WORKER)

    def __str__(self):
        return f"{self.staff} - {self.get_status_display()} - {self.date}"


class PositionLevel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Department(BaseModel):
    name = models.CharField(max_length=100)
    count_personal = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.count_personal} персонала)"


class WorkerSalaryPayed(BaseModel):
    total_amount_payed = models.IntegerField()
    datePayDay = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Оплачено: {self.total_amount_payed} в {self.datePayDay}"


class WorkerSalaryWaitedPay(BaseModel):
    worker = models.ForeignKey('Staff', on_delete=models.CASCADE, related_name='waiting_salaries', null=True, blank=True)
    total_amount = models.IntegerField()
    didnt_payed_days = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Ожидается: {self.total_amount} до {self.didnt_payed_days}"


class Staff(BaseModel):
    firstname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    live_place_address = models.TextField(max_length=100)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='workers')
    salary_pay = models.OneToOneField(WorkerSalaryPayed, on_delete=models.CASCADE)
    position = models.ForeignKey(PositionLevel, on_delete=models.SET_NULL, null=True)
    work_days = models.ManyToManyField(WorkDay, blank=True, related_name='staff_members')
    salary_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.firstname} {self.surname} - {self.position}"
