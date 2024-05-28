from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    interests=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    phone=models.IntegerField()
    image=models.ImageField(upload_to='students_images/', null=True, default=True)
    
    def __str__(self):
        return f'{self.first_name}'



    
class Hobby(models.Model):
    name=models.CharField(max_length=100)
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name='hobby')
    
    def __str__(self):
        return f'{self.name}'


