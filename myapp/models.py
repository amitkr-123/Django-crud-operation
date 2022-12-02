from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.CharField(max_length=10)
    _class = models.CharField(max_length=20)
    def __str__(self):
        return self.name