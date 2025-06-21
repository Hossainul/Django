from django.urls import path
from .views import userLogin,SignUpView,profile,Logout,changePass,changePasswithoutold,updateData,appPostclassbasedview,showPost,editPostView,deletePost,detailsView

urlpatterns = [
    path('login/',userLogin.as_view(), name = "Login"),
    path('signup/', SignUpView.as_view(), name = "signup"),
    path('profile/', profile, name = 'profile'),
    path('logout/', Logout, name = 'logout'),
    path('change/password/',changePass, name = 'changePass'),
    path('change/password/withou/old/one/',changePasswithoutold, name = "withoutold"),
    path('change/information/',updateData, name = "update_info"),
    path('add/post',appPostclassbasedview.as_view(), name = "addPost"),
    path('show/post',showPost, name = 'showPost'),
    path('edit/post/<int:id>',editPostView.as_view(), name = "edit_post"),
    path('delete/post/<int:id>',deletePost.as_view(), name = "delete_post"),
    path('details/<int:id>', detailsView.as_view(), name = "details"),

]
