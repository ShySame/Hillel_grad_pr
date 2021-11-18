from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from web_shop.models import Book
from .cart import Cart
from .forms import CartAddProductForm
from .tasks import email_send

User = get_user_model()


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', context={'cart': cart})


def confirm_order(request):
    email = User.objects.get(username=request.user).email
    try:
        email_send.apply_async(args=(email,))
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return render(request, 'email/confirm.html')
