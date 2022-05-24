from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('contact',views.contact,name='contact'),
    path('em',views.em,name='em'),
    path('hme',views.hme,name='hme'),
    path('lcd',views.lcd,name='lcd'),
    path('stepper',views.stepper,name='stepper'),
    path('ultra',views.ultra,name='ultra'),
]
