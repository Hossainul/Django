from django.shortcuts import render


def profile(req):
    return render(req,'profile.html');