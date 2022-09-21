from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello Django!")


def showIndex(request):
    params = {
        'title': 'Hello/Index/Page1',
        'msg': 'This is a sample page.',
        'goto': 'next',
    }

    return render(request, 'hello/index.html', params)


def next(request):
    params = {
        'title': 'Hello/Index/Page2',
        'msg': 'This is another page.',
        'goto': 'previous'
    }

    return render(request, 'hello/index.html', params)
