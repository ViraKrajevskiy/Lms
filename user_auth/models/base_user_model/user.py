from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class BaseModel(models.Model):
    created_ed = models.DateField(auto_now_add=True)
    updated_ed = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Поле ввода номера телефона не должно быть пустым!')
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_student(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault('role', 'student')
        return self.create_user(phone_number, email, password, **extra_fields)

    def create_worker(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault('role', 'worker')
        extra_fields.setdefault('is_staff', True)
        return self.create_user(phone_number, email, password, **extra_fields)

    def create_teacher(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault('role', 'teacher')
        return self.create_user(phone_number, email, password, **extra_fields)

    def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault('role', 'supervisor')
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(phone_number, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Админ'
        STUDENT = 'student', 'Студент'
        TEACHER = 'teacher', 'Преподаватель'
        WORKER = 'worker', 'Сотрудник'
        SUPERVISOR = 'supervisor', 'Глава'

    phone_regex = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Номер телефона должен быть в формате +998XXXXXXXX!"
    )
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=13, unique=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number

    def is_teacher(self):
        return self.role == self.Role.TEACHER

    def is_admin(self):
        return self.role == self.Role.ADMIN

    def is_student(self):
        return self.role == self.Role.STUDENT

    def is_worker(self):
        return self.role == self.Role.WORKER

    def is_supervisor(self):
        return self.role == self.Role.SUPERVISOR
