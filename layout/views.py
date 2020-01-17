from django.shortcuts import render

from django.http import HttpResponse

def layout(request):
    return render(request ,"Layout.html")

def index(request):
    return render(request ,"index.html")

def about(request):
    return render(request ,"about.html")

def service(request):
    return render(request ,"elements.html")

def contact(request):
    return render(request ,"contact.html")

def news(request):
    return render(request ,"news.html")

def destinations(request):
    return render(request ,"destinations.html")

