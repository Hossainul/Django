
from django.contrib import admin
from django.urls import path,include
from Blog_Project.views import homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage, name = "homePage"),
    path('Author/', include('Author.urls')),
    path('Post/', include('Post.urls')),
    path('Categories/', include('Categories.urls')),
    path('Profile/', include('Profile.urls')),
]
