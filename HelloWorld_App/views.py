from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHello(request):
    return HttpResponse('<h1 style="text-align: center">Hello, World!</h1>')
# Create your views here.
