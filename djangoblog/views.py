from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse('Hello World!')
    return render(request , 'about.html')

def home(request):
    # return HttpResponse('Home')
    return render(request , 'Home.html')
