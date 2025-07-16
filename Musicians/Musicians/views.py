from django.shortcuts import redirect,render


def homePage(req):
    return render(req,'home.html')