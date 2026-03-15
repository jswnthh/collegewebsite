from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blogPage, name="blog_page"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
]