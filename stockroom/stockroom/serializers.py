from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Author, Book, BookAuthor, BookInstance, Publisher

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'last_name', 'email']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = Author
        fields = ['pk', 'url', 'first_name', 'last_name', ]


class BookSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    author = serializers.CharField(required=True)

    class Meta:
        model = Author
        fields = ['pk', 'url', 'title', 'author', ]


class BookInstanceSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, required=True)
    cover = serializers.CharField(required=True)
    publisher = serializers.CharField(read_only=True)
    author = AuthorSerializer(many=True)
    date_of_receipt = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Author
        fields = ['pk', 'url', 'title', 'author', 'price', 'cover', 'publisher', 'date_of_receipt', ]


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Publisher
        fields = ['pk', 'url', 'name', ]
