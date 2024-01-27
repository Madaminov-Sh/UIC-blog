from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.PostsListsView.as_view()),
    path('post/<int:pk>/', views.PostDetailApiView.as_view()),
    path('categories/', views.CategoriesListsView.as_view()),

    path('tags/', views.TagsListsView.as_view()),
]