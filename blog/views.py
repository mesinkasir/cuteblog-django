from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.
class BlogPage (ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'post'
