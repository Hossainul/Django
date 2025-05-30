from django.urls import path
from .views import Login,signUp,profile,Logout,changePass,changePasswithoutold,updateData,addPOST,showPost,edit_post,delete

urlpatterns = [
    path('login/',Login, name = "Login"),
    path('signup/', signUp, name = "signup"),
    path('profile/', profile, name = 'profile'),
    path('logout/', Logout, name = 'logout'),
    path('change/password/',changePass, name = 'changePass'),
    path('change/password/withou/old/one/',changePasswithoutold, name = "withoutold"),
    path('change/information/',updateData, name = "update_info"),
    path('add/post',addPOST, name = "addPost"),
    path('show/post',showPost, name = 'showPost'),
    path('edit/post/<int:id>',edit_post, name = "edit_post"),
    path('delete/post/<int:id>',delete, name = "delete_post"),

]
