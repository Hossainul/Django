from django.shortcuts import render
from Musicians.forms import musician
from Album.models import addAlbum

def homepage(req):
    album_data = addAlbum.objects.all()
    return render(req,'home.html', {'data' : album_data})