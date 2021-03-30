from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'courses/index.html')


def first(request):
    return render(request, 'courses/page1.html')


def second(request):
    return render(request, 'courses/page2.html')
