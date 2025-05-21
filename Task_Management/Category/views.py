from django.shortcuts import render,redirect
from .forms import formCategories
from .models import categories

# Create your views here.
def addCategories(req):
    if req.method == "POST":
        form = formCategories(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('add_category')
    else :
        form = formCategories()
    
    return render(req,'add_categories.html',{'form' : form})


def Edit(req,id):
    fetching = categories.objects.get(pk = id)
    form_data = formCategories(instance=fetching)

    if req.method == 'POST':
        form = formCategories(req.POST, instance=fetching)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    
    else :
        return render(req,'add_categories.html',{'form' : form_data})
