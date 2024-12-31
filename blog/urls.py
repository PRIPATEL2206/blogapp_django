from django.urls import path
from .views import  all_blogs_view,blog_view

urlpatterns = [
    path('',all_blogs_view,name='all_blogs'),
    path('<slug:slug>/',blog_view,name='blog')
]