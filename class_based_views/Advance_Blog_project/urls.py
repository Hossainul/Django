
from django.contrib import admin
from django.urls import path,include
from .views import home

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name = "homepage"),
    path('category/<slug:category_slug>/',home, name = "category_wise_post"),
    path('Author/', include('Author.urls')),
    path('Category/', include('Category.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)