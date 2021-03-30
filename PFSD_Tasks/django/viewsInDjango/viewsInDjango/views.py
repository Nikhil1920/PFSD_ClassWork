from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Welcome to KlUniversity Index page</h1>")


def first(request):
    return HttpResponse("<h1>KLU UG Page-1</h1>")


def second(request):
    return HttpResponse("<h1>KLU UG Page-2</h1>")
