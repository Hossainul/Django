from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse("this is the courses page")
