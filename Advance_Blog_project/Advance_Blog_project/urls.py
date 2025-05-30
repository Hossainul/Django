
from django.contrib import admin
from django.urls import path,include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name = "homepage"),
    path('category/<slug:category_slug>/',home, name = "category_wise_post"),
    path('Author/', include('Author.urls')),
    path('Category/', include('Category.urls')),
]
