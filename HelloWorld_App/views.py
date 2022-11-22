from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHello(request):
    msg = '<h1 style="text-align: center">Hello, World!</h1'
    msg += 'h2 style="text-align: center">Hello, World!</h2>'
    msg += 'h3 style="text-align: center">Hello, World!</h3>'
    msg += 'h4 style="text-align: center">Hello, World!</h4>'
    msg += 'h5 style="text-align: center">Hello, World!</h5>'
    msg += 'h6 style="text-align: center">Hello, World!</h6>'
    msg += 'br/><br/><h2 style="text-align: center">Hello, < aan style="color:blue;">Christopher :-)</span></h2>'
    return HttpResponse(msg1)
# Create your views here.
