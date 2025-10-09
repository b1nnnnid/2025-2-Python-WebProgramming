from django.shortcuts import render, redirect
from . import models
from . import forms
from django.http import *

def index(request):
    if request.method == 'GET':
        students = models.Student.objects.all()
        form = forms.StudentForm()
        return render(request, 
                    'main/index.html',
                    {
                        'students': students,
                        'form': form
                    }
                )
    elif request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        else: raise HttpResponseNotAllowed('Bad Request')
    else:
        raise HttpResponseNotAllowed('Method not allowed')
