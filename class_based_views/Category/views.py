from django.shortcuts import render,redirect
from .forms import categoryForm

# Create your views here.

def addCategory(req):
    if req.method == 'POST':
        form = categoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = categoryForm()
    
    return render(req,'add_category.html', {'form' : form})