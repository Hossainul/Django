from django.shortcuts import render

def home(req):
    return render(req,'./for_myself/home.html')