from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'index.html', {'name': 'Jun'})


def login(request):
    return render(request, 'logo.html')
