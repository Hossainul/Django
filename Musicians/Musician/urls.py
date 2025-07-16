from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.signUp.as_view(), name ="register"),
    path('profile/',views.profile, name ="profile"),
    path('login/',views.CustomLoginView.as_view(), name = "login"),
    # path('change/password/',views.passwordChangeUser, name = "passwordchange"),
    path('change/password/without/old/one/',views.mypasswordchange.as_view(), name = "passwordchangewithout"),
    path('logout/confirm/', views.logout_confirm, name='logout_confirm'),
    path('logout/', views.logOUT, name='logout'),  # Actual logout action
    path('edit/profile',views.ProfileUpdateView.as_view(), name = "edit_profile"),
    path('add/album',views.addAlbum.as_view(), name = "add_album"),
    path('show/all/album',views.profileView.as_view(), name = "show_album"),
    path('show/all/album/delete/<int:pk>',views.deleteAlbum.as_view(), name = "delete_album"),
    path('show/all/album/edit/<int:pk>',views.editAlbum.as_view(), name = "edit_album"),
   

]
