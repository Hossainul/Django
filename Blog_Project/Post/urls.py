from django.urls import path,include
from Post.views import addPost,editpost,deletePost

urlpatterns = [
    path('addpost/',addPost, name ="add_post"),
    path('editpost/<int:id>',editpost, name ="edit_post"),
    path('deletepost/<int:id>',deletePost, name ="delete_post")
]
