from django.shortcuts import render
from django.shortcuts import HttpResponse


def home_view(request, *args, **kwargs):
    return render(request, 'hello.html', {})


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is context text",
        "my_number": 123,
        "my_list": [1, 4, 7, 8],
        "my_html": "<h1>Abouuuuut</h1>"
    }
    return render(request, 'about.html', my_context)

