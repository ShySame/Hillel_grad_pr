from shop.models import Author, Book, BookAuthor

from django.contrib import admin


class BookAuthorInline(admin.StackedInline):
    model = Book.author.through


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ordering = ['last_name', ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ordering = ['title', 'price', 'rating', ]
    list_filter = ['author', ]
    search_fields = ['title', 'author', ]
    inlines = [
        BookAuthorInline,
    ]


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('book', 'author')
