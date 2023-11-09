from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/', views.posts, name='posts'),
    path("post/<int:id>/", views.post, name="post"),
    path("categories", views.categories, name="categories"),
    path("category/<int:id>/", views.category, name="category"),
    path('search/', views.search, name='search'),
    path("register/", views.register, name='register'),
    path("post/<int:id>/comment", views.comment, name="comment"),
]