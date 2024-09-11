from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('initial/', views.initial, name='initial'),
    path('search_product/', views.search_product, name='search_product'),
    path('add_product/', views.add_product, name='add_product'),
]