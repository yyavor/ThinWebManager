from django.shortcuts import render
from django.shortcuts import HttpResponse


def home_view(*args, **kwargs):
    return HttpResponse('<h1>This is home view</h1>')
