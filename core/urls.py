from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_product, name='search_product'),
    path('add/', views.add_product, name='add_product'),
]