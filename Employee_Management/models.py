from django.db import models

# Create your models here.
class Employee_Management(models.Model):
    name=models.CharField(max_length=100)
    emo_id=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=10)