from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def how_it_works(request):
    return render(request, 'how-it-works.html')
