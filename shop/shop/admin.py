from shop.models import Author, Book, BookAuthor

from django.contrib import admin


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ordering = ['last_name', ]


class BookInline(admin.TabularInline):
    model = Book
    max_num = 3


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ordering = ['title', 'price', 'rating', ]
    list_filter = ['author', ]
    search_fields = ['title', 'author', ]
    inlines = [BookInline, ]


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('book', 'author')
