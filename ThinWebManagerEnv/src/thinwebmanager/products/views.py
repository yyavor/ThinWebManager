from django.shortcuts import render
from .models import Product


def product_detail_view(request):
    prod = Product.objects.get(id=1)
    context = {
        "prod": prod
    }
    return render(request, "products/detail.html", context)

