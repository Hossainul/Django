from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.

def add_musician(req):
    if req.method =="POST":
        form = forms.formMusicians(req.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('add_musician')
    else:
        form = forms.formMusicians()
    
    return render(req,'add_musicians.html', {'form' : form})

def edit_musicians(req,id):
    data = models.musician.objects.get(pk = id)
    form = forms.formMusicians(instance=data)

    if req.method == 'POST':
        form_data = forms.formMusicians(req.POST, instance = data)
        if form_data.is_valid():
            print(form_data.cleaned_data)
            form_data.save()
            return redirect('add_musician')
    
    else :
        return render(req,'add_musicians.html',{'form' : form})