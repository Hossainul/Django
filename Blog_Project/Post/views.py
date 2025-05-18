from django.shortcuts import render,redirect
from Post.forms import add_post
from Post.models import Post

# Create your views here.

def addPost(req):
    if req.method == 'POST':
        form = add_post(req.POST)
        
        if form.is_valid():
            print(form)
            form.save()
            return redirect('add_post')
    else:
        form = add_post()

    return render(req,'addpost.html', {'form' : form})

def editpost(req,id):

    edit_form = Post.objects.get(pk = id)
    form = add_post(instance = edit_form)
    

    if req.method == 'POST':
        form = add_post(req.POST, instance = edit_form)
        
        if form.is_valid():
            print(form)
            form.save()
            return redirect('homePage')
    else:
      return render(req,'addpost.html', {'form' : form})


def deletePost(req,id):
    form = Post.objects.get(pk = id)
    form.delete()
    return redirect('homePage')