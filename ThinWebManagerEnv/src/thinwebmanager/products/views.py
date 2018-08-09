from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm


def product_create_view(request):
    product_form = ProductForm(request.POST or None)
    if product_form.is_valid():
        product_form.save()
        product_form = ProductForm()

    context = {
        "form": product_form
    }
    return render(request, "products/product_create.html", context)


def product_update_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_form = ProductForm(request.POST or None, instance=product)
    if product_form.is_valid():
        product_form.save()
    context = {
        "form": product_form
    }
    return render(request, "products/product_create.html", context)


def product_delete_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect("../")
    context = {
        "product": product
    }
    return render(request, "products/product_delete.html", context)


def products_list_view(request):
    query_set = Product.objects.all()
    context = {
        "products": query_set
    }
    return render(request, "products/products_list.html", context)


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        "product": product
    }
    return render(request, "products/product_detail.html", context)







