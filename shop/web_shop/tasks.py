from celery import shared_task

import requests

from .models import Author, Book, BookAuthor, \
    Category, CategoryBook, Order, OrderHistory

BASE_URL = 'http://stockroom:8001/v1/api/'
AUTHOR_ENDPOINT = 'authors/'
BOOK_ENDPOINT = 'books/'
BOOK_INST_ENDPOINT = 'bookinst/'


@shared_task
def data_task():
    author_add()
    book_add()


def author_add():
    author_list = []
    author_request = requests.get(BASE_URL + AUTHOR_ENDPOINT)
    data = author_request.json()

    # next page link
    next_page = data['next']

    for i in range(len(data['results'])):
        author_name = data['results'][i]['name']
        author_list.append(Author(name=author_name))
    print(author_list)


def book_add():
    pass


data_task()
