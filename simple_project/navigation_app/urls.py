from django.urls import path,include
from . import views

urlpatterns = [
   path("mPage/",views.mPage),
   path("sPage/",views.Spage),
   path("showData/",views.showData)
]
