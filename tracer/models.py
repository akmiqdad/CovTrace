from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from datetime import date

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False,default="")
    name=models.CharField(max_length=30, blank=False)
    admnno=models.CharField(max_length=10, blank=False)
    designation=models.CharField(max_length=15, blank=False)
    sclass=models.CharField(max_length=10, blank=False)
    age=models.IntegerField()
    phone=models.IntegerField()
    health=models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.user.username

        
