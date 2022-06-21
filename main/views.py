from django.shortcuts import render
from django.http import HttpResponse

def index(reqest):
    data = {

        'val': ['wer', 'ret', 'info']
    }


    return render(reqest, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def cont(request):
    return render(request, 'main/contact.html')

def one(request):
    return render(request, 'main/one.html')

