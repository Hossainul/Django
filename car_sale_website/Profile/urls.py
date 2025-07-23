from django.urls import path
from . import views


urlpatterns = [
    path('profile/',views.userProfile, name = "profile"),
    path('password/change/', views.passwordChange.as_view(), name = "passwordchange"),
    path('logout/confirmation/',views.logout_confirm, name = "logout_confirmation"),
    path('logout/',views.logout_user, name = "logout"),
    path('profile/edit/<int:pk>/',views.editProfile.as_view(), name = "edit_profile"),
    path('profile/see/all/cars/', views.allCars.as_view(), name = "all_cars"),
    path('profile/buy/car/<int:car_id>/', views.buyCar.as_view(), name = "buy_car"),
    path('user/history/', views.UserHistoryView.as_view(), name='user_history'),
]
