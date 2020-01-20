from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.layout, name='layout'),
    path('about/', views.about,name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('destinations/', views.destinations, name='destinations'),
    path('registration/', views.registration, name='registration'),
]