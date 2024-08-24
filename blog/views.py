from django.shortcuts import render
from .models import BlogPost

def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})
