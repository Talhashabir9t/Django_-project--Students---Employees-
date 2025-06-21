from django.db import models

# Create your models here.

class Employee(models.Model):
    Emp_id=models.CharField(max_length=20)
    Name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)

    def __str__(self):
        return self.Name