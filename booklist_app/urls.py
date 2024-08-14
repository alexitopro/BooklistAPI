from django.urls import path
from . import views

# Define the URL patterns for the booklist_app
urlpatterns = [
    path('books/', views.books),
]