from django.shortcuts import render,redirect
from Author.forms import Add_author

# Create your views here.

def addAuthor(req):
    if req.method == "POST":
        form = Add_author(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('add_author')
    else:
        form = Add_author()

    return render(req, "add_author.html", {'form' : form})