from django.shortcuts import render,redirect
from Album.forms import addalbumForm
from Album.models import addAlbum

# Create your views here.

def add_album(req):
    if req.method == "POST":
        form = addalbumForm(req.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('add_album')
    else:
        form = addalbumForm()
    
    return render(req,'add_album.html', {'form' : form})

def edit_album(req,id):
    album = addAlbum.objects.get(pk = id)
    form_data = addalbumForm(instance=album)
    
    if req.method == 'POST':
        form = addalbumForm(req.POST, instance = album)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else :
        return render(req,'add_album.html', {'form' : form_data})
    
def delete_album(req,id):
    form = addAlbum.objects.get(pk = id)
    form.delete()
    return redirect("homepage")