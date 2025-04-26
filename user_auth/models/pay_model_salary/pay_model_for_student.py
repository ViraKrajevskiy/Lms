from django.db import models
from django.db.models import *

from user_auth.models.base_user_model.user import BaseModel

class StudentPay(BaseModel):
    PAYMENT_TYPE_CHOICES = [
        ('Cr', 'Картой'),
        ('Mn', 'Наличкой'),
    ]

    payment_type = models.CharField(choices=PAYMENT_TYPE_CHOICES, max_length=2)
    value = models.CharField(max_length=40, blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    course_pay = ForeignKey('Course',on_delete=models.SET_NULL,null=True, blank=True, related_name='payments')
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='payments')

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.payment_type == 'Cr' and not self.card_number:
            raise ValidationError("Номер карты обязателен для оплаты картой.")
        if self.payment_type == 'Mn' and self.card_number:
            raise ValidationError("Номер карты не должен быть указан для наличной оплаты.")

