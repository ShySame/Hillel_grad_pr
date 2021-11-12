import json
import random
import sys

from stockroom.models import Author, Book, BookAuthor, \
    BookInstance, Category, CategoryBook, Publisher

from faker import Faker

fake = Faker()
import requests

from django.core.management.base import BaseCommand, CommandError

SITE = 'https://poetrydb.org/author/'


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            # ch = list(Category.objects.values_list('id', flat=True))

            author_li, book_li, bookinst_li, cat_li, booka_li = [], [], [], [], []
            # for i in Book.objects.values_list('id', flat=True):
            #     g = random.sample(ch, 3)
            #     for j in range(random.randint(1, 3)):
            #         cat_li.append(CategoryBook(category_id=g[j-1],
            #                                     book_id=i))
            # CategoryBook.objects.bulk_create(cat_li)

            # for _ in range(2000):
            #     bookinst_li.append(BookInstance(ISBN=fake.isbn13(),
            #                                     price=round(random.uniform(10.50, 100.50), 2),
            #                                     cover=random.choice(['Hard', 'Soft']),
            #                                     publisher_id=random.choice(
            #                                         Publisher.objects.values_list('id', flat=True)),
            #                                     title_id=random.choice(Book.objects.values_list('id', flat=True))))
            #
            # BookInstance.objects.bulk_create(bookinst_li)

            # for i in list(Author.objects.values_list('name', flat=True)):
            #     url = SITE + i
            #     r = requests.get(url)
            #     data = json.loads(r.content)
            #     for j in range(len(data)):
            #         book_li.append(Book(title=data[j]['title']))
            # Book.objects.bulk_create(book_li)

            # author_id=list(Author.objects.values_list('id', flat=True))
            # k=1
            # for i in author_id:
            #     url = SITE + Author.objects.get(pk=i).name
            #     r = requests.get(url)
            #     data = json.loads(r.content)
            #     for j in range(len(data)):
            #         booka_li.append(BookAuthor(author_id=i,
            #                                    book_id=k))
            #         k+=1

            # BookAuthor.objects.bulk_create(booka_li)
        except (Author.DoesNotExist or Book.DoesNotExist
                or BookInstance.DoesNotExist or CategoryBook.DoesNotExist):
            raise CommandError('Smth wrong :(')
