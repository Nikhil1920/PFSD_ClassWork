from django.shortcuts import render


def index(request):
    return render(request, 'djangofirst/index.html')


def first(request):
    return render(request, 'djangofirst/first.html')


def second(request):
    return render(request, 'djangofirst/second.html')
