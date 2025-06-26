from django.db import models

class Library(models.Model):
    address = models.CharField(max_length=300)
    name = models.CharField(max_length=200)

class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()

class BookData(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books')
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    page_count = models.PositiveIntegerField()

class Book(models.Model):
    book_data = models.ForeignKey('BookData', on_delete=models.CASCADE, related_name='books')
    library = models.ForeignKey('Library', on_delete=models.CASCADE, related_name='books')








