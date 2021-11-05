from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Book(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ManyToManyField(Author, through='BookAuthor')
    rating = models.FloatField(default=0)

    def __str__(self):
        return f'{self.title}'


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)