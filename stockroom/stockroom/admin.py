from .models import Author, Book, BookAuthor, BookInstance, \
    Category, CategoryBook, Publisher

from django.contrib import admin


class BookAuthorInline(admin.StackedInline):
    model = Book.author.through


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ['name', ]
    inlines = [
        BookAuthorInline,
    ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ordering = ('title', 'category',)
    search_fields = ('title',)
    inlines = [
        BookAuthorInline,
    ]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    ordering = ['ISBN', 'title', 'price', ]
    search_fields = ['title', ]
    date_hierarchy = 'date_of_receipt'

    fieldsets = (
        ('Info',
         {
             'fields': ('ISBN', 'title')
         }),
        ('Price',
         {
             'fields': ('price',)
         }),
        ('',
         {
             'fields': ('rating', 'cover')
         }),
        ('Publisher',
         {
             'fields': ('publisher',)
         }),
        ('Date of receipt',
         {
             'fields': ('date_of_receipt',)
         })
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)


@admin.register(CategoryBook)
class CategoryBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'category')


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('book', 'author')
