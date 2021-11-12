from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.category}'


COVERS = (
    ('Hard', 'Hard cover'),
    ('Soft', 'Soft cover')
)


class Book(models.Model):
    category = models.ManyToManyField(Category, through='CategoryBook')
    title = models.CharField(max_length=250)
    author = models.ManyToManyField(Author, through='BookAuthor')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.CharField(max_length=4, choices=COVERS)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return f'{self.title}'


class CategoryBook(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'


class BookInstance(models.Model):
    ISBN = models.CharField(max_length=17)
    title = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    date_of_receipt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ISBN}: {self.title} - {self.publisher}'


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
