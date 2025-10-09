from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    student_id = models.CharField(max_length=13, unique=True)
    
    #유수빈(20220447)
    
    def __str__(self):
        return f"{self.name} ({self.student_id})"