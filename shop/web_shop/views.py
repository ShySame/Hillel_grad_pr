import requests
from django.views import generic

from cart.forms import CartAddProductForm
from .models import Author, Book, Category, CategoryBook


class IndexView(generic.TemplateView):
    template_name = 'shop/index.html'


class BookView(generic.ListView):
    model = Book
    template_name = 'shop/book_list.html'

    def get_queryset(self, ):
        filter_text = self.request.GET.get("filter")
        search_text = self.request.GET.get("search")
        if filter_text:
            return Book.objects.filter(
                categorybook__category=Category.objects.get(
                    category=filter_text
                ))
        elif search_text:
            return Book.objects.filter(title__icontains=search_text)
        else:
            return Book.objects.all()


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'shop/book_detail.html'

    def get_context_data(self, **kwargs):
        queryset = Book.objects.get(id=self.object.id).author.all()
        contex = super().get_context_data()
        contex['queryset'] = queryset
        cart_product_form = CartAddProductForm()
        contex['cart'] = cart_product_form
        return contex


class CategoryList(generic.ListView):
    model = Category
    template_name = 'shop/category_list.html'
