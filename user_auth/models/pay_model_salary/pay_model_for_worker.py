from django.db import models
from rest_framework.fields import DateTimeField
from user_auth.models.base_user_model.user import BaseModel
from user_auth.models.workers_models.model_worker import Staff


class PyedForWorker(BaseModel):
    card_number = models.CharField(max_length=16, blank=True, null=True)
    work_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)  # Установи default здесь
    balance = models.OneToOneField(Staff, on_delete=models.CASCADE)


    def save(self, *args, **kwargs,):
        if not self.pk:
            self.balance.salary_balance += self.amount
            self.balance.save()
        super().save(*args, **kwargs)
