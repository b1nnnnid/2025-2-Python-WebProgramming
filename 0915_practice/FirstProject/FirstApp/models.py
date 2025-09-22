from django.db import models

class Author(models.Model):
    name = models.CharField( max_length = 100)
    birth_date = models.DateField(null = True, blank = True)
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    publisihed_date = models.DateField()
    isbn = models.CharField(max_length = 13,unique = True)
    
    def __str__(self):
        return self.title
    
    
class Student(models.Model):
    name=models.CharField(max_length= 100)
    student_id= models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return f"{self.name}({self.student_id})"