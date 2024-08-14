from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Book
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

@csrf_exempt
def books(request):
    if request.method == 'GET':
        # Get all the books from the database
        books = Book.objects.all().values()
        # Convert the books to a dictionary
        books_dict = {'books': list(books)}
        # Return the books as JSON
        return JsonResponse(books_dict)
    elif request.method == 'POST':
        # Get the title, author, and price from the request
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        # Create a new book object
        book = Book(
            title = title,
            author = author,
            price = price
        )
        
        try:
            # Save the book to the database
            book.save()
        except IntegrityError:
            # Return an error
            return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)
        
        # Return the book as JSON with a status of 201 (created)
        return JsonResponse(model_to_dict(book), status = 201)