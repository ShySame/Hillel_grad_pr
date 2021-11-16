from .models import Author, Book, BookAuthor, BookInstance, \
    Category, CategoryBook, Publisher

from django.contrib import admin


class BookAuthorInline(admin.StackedInline):
    model = Book.author.through


class BookCategoryInline(admin.TabularInline):
    model = Book.category.through


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = ['name', ]
    inlines = [
        BookAuthorInline,
    ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', )
    ordering = ('title',)
    radio_fields = {'cover': admin.VERTICAL}
    search_fields = ('title',)
    inlines = [
        BookAuthorInline,
        BookCategoryInline,
    ]



@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'ISBN', 'title', 'date_of_receipt',)
    ordering = ['ISBN', 'title', ]
    search_fields = ['title', ]
    date_hierarchy = 'date_of_receipt'
    readonly_fields = ['date_of_receipt', ]

    fieldsets = (
        ('Info',
         {
             'fields': ('ISBN', 'title')
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
    list_display = ('id', 'category',)
    inlines = [
        BookCategoryInline,
    ]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(CategoryBook)
class CategoryBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'category')


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('book', 'author')
