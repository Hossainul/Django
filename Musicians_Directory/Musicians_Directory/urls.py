
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name = "homepage"),
    path('musicians/',include("Musicians.urls")),
    path('album/',include("Album.urls")),
]
