from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 1cac95aa is the polls index.")