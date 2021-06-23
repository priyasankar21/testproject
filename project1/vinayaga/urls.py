from django.urls import path
from . import views
from .import forms
  
urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/home/', views.home, name='home'),
    path('index/sell/', views.sells, name='sells'),
    path('buy/<str:m_name>', views.buy, name='buy'),
     path('index/contact/', views.contact, name='contact'),
]
