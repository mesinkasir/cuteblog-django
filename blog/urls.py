from django.urls import path
from .views import BlogPage, PostDetailView 
 
urlpatterns = [
    path('',BlogPage.as_view() , name='blog'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post')
]

