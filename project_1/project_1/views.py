from django.http import HttpResponse
from django.shortcuts import render


def contact(request):
    return HttpResponse("This is contact")

# def home(request):
#     return HttpResponse("this is homepage")

def home(request):
    return render(request,'index.html')