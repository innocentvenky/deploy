from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_id=models.IntegerField()
    phone_no=models.CharField(max_length=14)
    salary=models.FloatField()
    address=models.TextField()