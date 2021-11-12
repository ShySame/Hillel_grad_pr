from .models import Author, Book, BookAuthor, \
    Category, CategoryBook, Order, OrderHistory

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
    list_display = ('id', 'title', 'price', 'available', 'rating',)
    ordering = ('title', 'price',)
    search_fields = ('title', 'available')
    inlines = [
        BookAuthorInline,
        BookCategoryInline,
    ]

    fieldsets = (
        ('Info',
         {
             'fields': ('title',)
         }),
        ('Price',
         {
             'fields': ('price', 'available')
         }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category',)
    inlines = [
        BookCategoryInline,
    ]


@admin.register(CategoryBook)
class CategoryBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'category')


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('book', 'author')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'quantity')


@admin.register(OrderHistory)
class OrderHistoryAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'quantity', 'date')
    date_hierarchy = 'date'
