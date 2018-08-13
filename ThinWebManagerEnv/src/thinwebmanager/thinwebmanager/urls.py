from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from pages.views import home_view, contact_view, about_view

urlpatterns = [
    path('products/', include('products.urls')),
    path('blog/', include('blog.urls')),
    url(r'^chat/', include('chat.urls')),
    path('', home_view, name='home'),
    path('about/', about_view),
    path('contact/', contact_view),
    path('admin/', admin.site.urls)
]
