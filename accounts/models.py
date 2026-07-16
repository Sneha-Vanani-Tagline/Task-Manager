from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    class UserOption(models.TextChoices):
        Admin = 'admin', 'Admin'
        Manager = 'manager', 'Manager'
        Employee = 'employee', 'Employee'
    
    role = models.CharField(max_length=20,choices=UserOption)
    



