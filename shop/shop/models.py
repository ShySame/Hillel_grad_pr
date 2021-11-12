from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

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
    title = models.CharField(max_length=250)
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


class Order(models.Model):
    book_id = models.ManyToManyField(Book)
    quantity = models.PositiveSmallIntegerField(default=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderHistory(models.Model):
    book_id = models.ManyToManyField(Book)
    quantity = models.PositiveSmallIntegerField(default=1)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'History of orders'
