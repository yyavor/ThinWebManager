from django.urls import path
from .views import product_detail_view, product_create_view, product_update_view, product_delete_view,\
    products_list_view

app_name = "products"
urlpatterns = [
    path('', products_list_view, name="products-list"),
    path('create/', product_create_view, name="product-create"),
    path('<int:product_id>/', product_detail_view, name="product-detail"),
    path('<int:product_id>/delete/', product_delete_view, name="product-delete"),
    path('<int:product_id>/update/', product_update_view, name="product-update"),
]
