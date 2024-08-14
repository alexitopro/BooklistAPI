from django.db import models

# Create your models here.

# Create a model for the Book which as three attributes:
# title, author, price
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    # Create an index on the price field
    class Meta:
        indexes = [models.Index(fields=['price']),]

    # Define the string representation of the model
    def __str__(self):
        return self.title