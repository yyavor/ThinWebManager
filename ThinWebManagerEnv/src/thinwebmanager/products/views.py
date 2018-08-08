from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm


def render_initial_data(request):
    initial_data = {
        "title": "Awesome Title",
        "description": "Awesome Description",
    }
    obj = Product.objects.get(id=1)
    my_form = ProductForm(request.POST or None, instance=obj)
    if my_form.is_valid():
        my_form.save()
    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    prod = Product.objects.get(id=1)
    context = {
        "prod": prod
    }
    return render(request, "products/product_detail.html", context)


def dynamic_detail_view(request, prod_id):
    prod = Product.objects.get(id=prod_id)
    context = {
        "prod": prod
    }
    return render(request, "products/product_detail.html", context)

