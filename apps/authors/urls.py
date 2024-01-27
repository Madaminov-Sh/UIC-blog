from django.urls import path

from . import views

urlpatterns = [
    path('authors/', views.AuthorsListsApiView.as_view()),
    path('author/<int:pk>/', views.AuthorDetailApiView.as_view()),
]