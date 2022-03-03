from django.db import models

# Create your models here.

class student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    marks=models.IntegerField()
    subject=models.CharField(max_length=30)
    def __repr__(self):
        return self.first_name