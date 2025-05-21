
from django.contrib import admin
from django.urls import path,include
from .views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name = "homepage"),
    path('task/',include('Task.urls')),
    path('Category/',include('Category.urls'))
]
