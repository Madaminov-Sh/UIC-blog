from django.urls import path

from . import views

urlpatterns = [
    path('authors/', views.AuthorsListsApiView.as_view())
]