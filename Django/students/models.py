from django.db import models

# Create your models here.

class Student(models.Model):
    students_id=models.CharField(max_length=10)
    Name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)

    def __str__(self):
        return self.Name