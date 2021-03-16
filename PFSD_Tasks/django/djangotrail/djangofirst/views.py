from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi Django, we got you there.")
