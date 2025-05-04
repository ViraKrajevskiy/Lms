from django.db import models
from django.utils import timezone

#otp для смены пароля
class OTPCode(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def is_expired(self):
        return timezone.now() > self.created_at + timezone.timedelta(minutes=10)

    def __str__(self):
        return f"{self.user.phone_number} , {self.code}"
