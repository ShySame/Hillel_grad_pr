from django.contrib.auth import get_user_model

from rest_framework import viewsets

from .models import Author, Book, BookAuthor, BookInstance, Category, Publisher
from .serializers import AuthorSerializer, BookSerializer, BookAuthorsSerializer, \
    BookInstanceSerializer, CategorySerializer, PublisherSerializer, UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer


class BookAuthorViewSet(viewsets.ModelViewSet):
    queryset = BookAuthor.objects.all().order_by('author_id')
    serializer_class = BookAuthorsSerializer


class BookInstanceViewSet(viewsets.ModelViewSet):
    queryset = BookInstance.objects.all().order_by('title')
    serializer_class = BookInstanceSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('category')
    serializer_class = CategorySerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by('name')
    serializer_class = PublisherSerializer
