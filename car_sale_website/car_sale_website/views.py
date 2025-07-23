from django.urls import path 
from django.shortcuts import redirect,render

def homepage(req):
    return render('req', 'home.html')
