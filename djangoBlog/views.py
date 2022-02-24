from django.shortcuts import render
from django.shortcuts import HttpResponse
# HttpResponse : get request -> show value in it

def about(request):
    # return HttpResponse('Hi there!')
    return render(request, 'about.html')

def home(request):
    # return HttpResponse('Home')
    return render(request, 'Home.html')
