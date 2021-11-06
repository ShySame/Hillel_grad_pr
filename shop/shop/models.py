from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.category}'


class Author(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    category = models.ManyToManyField(Category, through='CategoryBook')
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    author = models.ManyToManyField(Author, through='BookAuthor')
    rating = models.FloatField(default=0)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return f'{self.title}'


class CategoryBook(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
