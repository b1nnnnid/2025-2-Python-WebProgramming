from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'department', 'student_id']
        labels = {
            'name' : '이름',
            'department' : '학과',
            'student_id' : '학번',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'이름'}),
            'department': forms.TextInput(attrs={'placeholder':'학과'}),
            'student_id': forms.TextInput(attrs={'placeholder':'학번'}),
        }