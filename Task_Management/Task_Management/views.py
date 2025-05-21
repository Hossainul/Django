from django.shortcuts import render,redirect
from Task.models import AddTask

def homepage(req):
    data = AddTask.objects.all()
    return render(req,'home.html', {'data': data})

