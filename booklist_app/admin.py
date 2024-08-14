from django.contrib import admin
from .models import Book

# Register your models here.

# Register the Book model with the admin site so we can view and edit the Book model from the admin site
admin.site.register(Book)