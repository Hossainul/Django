from django.shortcuts import render
from Post.models import Post

def homePage(req):
    data = Post.objects.all()
    print(data)
    return render(req,'home.html', {'data' : data})
