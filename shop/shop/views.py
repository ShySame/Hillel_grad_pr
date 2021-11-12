from django.views import generic
from .models import Author, Book, Category


class IndexView(generic.TemplateView):
    template_name = 'shop/index.html'


class BookView(generic.ListView):
    model = Book

    def get_queryset(self, ):
        filter_text = self.request.GET.get("filter")
        return Book.objects.filter(
            category__book__category=Category.objects.get(category=filter_text))


class CategoryList(generic.ListView):
    model = Category
    template_name = 'shop/category_list.html'
