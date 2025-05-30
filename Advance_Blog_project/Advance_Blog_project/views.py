from django.shortcuts import render
from Author.models import addPost
from Category.models import add_category

def home(req, category_slug=None):
    # Get all posts (filtered by category if slug provided)
    posts = addPost.objects.all()
    if category_slug:
        category = add_category.objects.get(slug=category_slug)
        posts = posts.filter(category=category)
    
    # Get all distinct categories for sidebar
    categories = add_category.objects.all()
    
    return render(req, 'home.html', {
        'data': posts,
        'categories': categories  # Add this line
    })