from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    # path('add/', views.add, name='add'),
    # path('contact/', views.contact, name='contact'),
]