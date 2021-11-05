from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ManyToManyField(Author, through='BookAuthor')

    def __str__(self):
        return f'{self.title} - {self.author}'


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'


COVERS = (
    ('Hard', 'Hard cover'),
    ('Soft', 'Soft cover')
)


class BookInstance(models.Model):
    title = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.CharField(max_length=4, choices=COVERS)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    date_of_receipt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.publisher}: {self.date_of_receipt}'


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
