from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def validation(request):
    return render(request, 'pages/validation.html')


def forecast(request):
    return render(request, 'pages/forecast.html')


def models(request):
    return render(request, 'pages/models.html')
