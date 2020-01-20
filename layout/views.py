from django.shortcuts import render, redirect
from .models import Destination
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

def layout(request):
    return render(request ,"Layout.html")

def index(request):

   # dest1 = Destination()
   # dest1.name = 'Delhi'
   # dest1.description = 'Delhi Dill Walo ki'
   # dest1.offer = True
   # dest1.price = 700
   # dest1.img = 'destination_1.jpg'

   # dest2 = Destination()
   # dest2.name = 'Mumbai'
  #  dest2.description = 'the city never sleep'
   # dest2.offer = False
   # dest2.price = 750

  #  dest3 = Destination()
  #  dest3.name = 'chennai'
   # dest3.description = 'Chennai Express'
   # dest3.offer = True
   # dest3.price = 650

  #  dest4 = Destination()
   # dest4.name = 'Bangalore'
   # dest4.description = 'IT Industry'
    #dest4.offer = True
    #dest4.price = 800

   # dest5 = Destination()
   # dest5.name = 'Kolkata'
   # dest5.description = 'Mamta didi ka raj'
  #  dest5.offer = False
   # dest5.price = 550

   # dest6 = Destination()
   # dest6.name = 'Uttarakhand'
   # dest6.description = 'Devo ki Dev Bhoomi'
    #dest6.offer = False
   # dest6.price = 600

   # dest7 = Destination()
  #  dest7.name = 'Jammu & Kashmir'
   # dest7.description = 'switzerland Of India'
   # dest7.offer = True
   # dest7.price = 900

   # dest8 = Destination()
   # dest8.name = 'Bali'
   # dest8.description = 'Nulla pretium tincidunt felis, nec.'
   # dest8.offer = True
    #dest8.price = 679

   # dest = [dest8, dest1, dest2, dest3, dest4, dest5, dest6, dest7]
    dest = Destination.objects.all()
    return render(request ,"index.html",{"Dest1":dest})


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

def registration(request):

    if request.method== 'post':
        username=request.POST['username']
        first_name=request.POST['first']
        last_name=request.POST['last']
        email=request.POST['email']
        password=request.POST['Password']
        user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        User.save()
    return render(request ,"registration.html")



