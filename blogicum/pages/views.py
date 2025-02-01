
from django.shortcuts import render

# Create your views here.
app_name = 'pages'


def about(request):
    return render(request, 'pages/about.html')


def rules(request):
    return render(request, 'pages/rules.html')
