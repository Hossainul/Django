from django.urls import path
from .views import signup_form,user_login,profile,Logout,passChange,withoutOld,updateEdit

urlpatterns = [
    path('signup/',signup_form, name = "signup_form"),
    path('login/',user_login, name = "login_form"),
    path('profile/',profile, name = "profile"),
    path('logout/',Logout, name = "logout"),
    path('password/change',passChange, name = 'passwordChange'),
    path('password/change/without/old/one',withoutOld, name = "withoutOld"),
    path('update/information',updateEdit, name = "update_info")
]
