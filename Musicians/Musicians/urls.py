
from django.contrib import admin
from django.urls import path,include
from Musician.views import allAlbumViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",allAlbumViews.as_view(), name = "homepage"),
    path("Musicians/", include("Musician.urls")),
   
]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
