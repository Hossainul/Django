
from django.contrib import admin
from django.urls import path,include
from .views import homepage
from django.conf.urls.static import static
from django.conf import settings
from Car import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include("Car.urls")),
    path('user/', include("User.urls")),
    path('user/', include("Profile.urls")),
    path('',views.carViews.as_view(), name = "homepage"),
]


urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)