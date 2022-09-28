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


def top(request):
    params = {
        'title': 'Hello/Top',
        'msg': 'Write your name.',
    }

    return render(request, 'hello/form.html', params)


def form(request):
    # inputタグのname属性で指定
    username = request.POST.get('msg')
    params = {
        'title': 'Hello/Form',
        'msg': 'Hello' + username + 'Nice to meet you.'
    }

    return render(request, 'hello/form.html', params)
