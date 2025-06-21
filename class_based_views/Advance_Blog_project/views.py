# Category/views.py
from django.shortcuts import render, get_object_or_404
from Author.models import addPost
from Category.models import add_category

def home(req, category_slug=None):
    posts = addPost.objects.all()
    categories = add_category.objects.all()

    if category_slug:
        category = get_object_or_404(add_category, slug=category_slug)
        posts = posts.filter(category=category)

    context = {
        'data': posts,
        'categories': categories,
    }
    return render(req, 'home.html', context)


