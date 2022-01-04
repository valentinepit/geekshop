from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def index(request):
    context = {
        "title": 'Главная',
        'products': Product.objects.all()[:4]
    }
    return render(request, 'mainapp/index.html', context=context)


def contact(request):
    context = {
        "title": 'Контакты'
    }
    return render(request, 'mainapp/contact.html', context=context)


links_menu = [
    {
        'url': 'products',
        'title': 'Все'
    },
    {
        'url': 'products_home',
        'title': 'дом'
    }, {
        'url': 'products_office',
        'title': 'офис'
    }, {
        'url': 'products_modern',
        'title': 'модерн'
    },
    {
        'url': 'products_classic',
        'title': 'классика'
    }
]


def products(request, pk=None):
    context = {
        'links_menu': ProductCategory.objects.all(),
        "title": "Продукты"
    }
    return render(request, 'mainapp/products.html', context=context)



