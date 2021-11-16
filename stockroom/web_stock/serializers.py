from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Author, Book, BookAuthor, BookInstance, Category, CategoryBook, Publisher

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'last_name', 'email']


class BookAuthorsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    book = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = BookAuthor
        fields = ['pk', 'author', 'book', ]


class CategoryBookSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.category')

    class Meta:
        model = CategoryBook
        fields = ['pk', 'category', ]


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    book = BookAuthorsSerializer(source='bookauthor_set', many=True)

    class Meta:
        model = Author
        fields = ['pk', 'url', 'name', 'book', ]


class BookSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    author = BookAuthorsSerializer(source='bookauthor_set', many=True)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, required=True)
    cover = serializers.CharField(required=True)
    category = CategoryBookSerializer(source='categorybook_set', many=True)

    class Meta:
        model = Book
        fields = ['pk', 'url', 'title', 'author', 'price',
                  'cover', 'category', ]


class BookInstanceSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    ISBN = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    publisher = serializers.CharField(read_only=True)
    date_of_receipt = serializers.DateTimeField(read_only=True)

    class Meta:
        model = BookInstance
        fields = ['pk', 'url', 'ISBN', 'title', 'publisher', 'date_of_receipt', ]


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Publisher
        fields = ['pk', 'url', 'name', ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    category = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = ['pk', 'url', 'category', ]
