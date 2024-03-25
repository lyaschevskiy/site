from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import ProductCategory, Product, Basket
from django.core.paginator import Paginator


def index(request: HttpRequest) -> HttpResponse:
    context = {'title': 'Store'}
    return render(request, 'products/index.html', context)


def products(request: HttpRequest, category_id=None, page_number=1) -> HttpResponse:
    product = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator = Paginator(product, per_page)
    product_paginator = paginator.page(page_number)
    context = {
        'title': 'Store - Каталог',
        'products': product_paginator,
        'categories': ProductCategory.objects.exclude(p_category__isnull=True),
    }
    return render(request, 'products/products.html', context)


def product_index(request: HttpRequest, product_id: int):
    product = Product.objects.filter(pk=product_id).first()
    context = {
        'title': product.name,
        'product': product
    }
    return render(request, 'products/product.html', context)


@login_required
def basket_add(request, product_id):
    Basket.create_or_add(product_id, request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_update(request, product_id):
    quantity_goods = request.POST.get('basketQuantity')
    Basket.update_quantity(product_id, quantity_goods, request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
