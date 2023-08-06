from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.

# ------------- 09-04-2023 ---------------------------
class User(AbstractUser):
    ROLE_CHOICES=[('Admin','Admin'),
                  ('Student','Student'),
                  ('Teacher','Teacher'),]
    role=models.CharField(max_length=10,choices=ROLE_CHOICES,default='Admin')
# ----------------------------------------------------------


class Student(models.Model):
    GENDER_CHOICES = [ ('Male' , 'Male'), ('Female', 'Female'),]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,blank=True)
    dob = models.DateField(default=datetime.now, blank=True)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,default='Male',)
    remarks = models.TextField(default='', blank=True)

    def __str__(self):
        return f'{self.id} {self.name}'

