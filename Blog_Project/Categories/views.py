from django.shortcuts import render,redirect
from Categories.forms import add_categories

# Create your views here.

def add_categori(request):
    if request.method == "POST":
        form = add_categories(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('add_categories')
    else:
        form = add_categories()
    
    return render(request,"add_categories.html", {'form' : form})
