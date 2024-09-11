from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login as auth_login
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

def initial(request):
    return render(request, 'initial.html')

def search_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name', '').strip()

        if product_name:
            product = Product.objects.filter(name__icontains=product_name).first()

            if product:
                return render(request, 'product_exists.html', {'product': product})
            else:
                return render(request, 'product_exists.html', {'error': 'No product found.'})
        else: 
            return render(request, 'search_product.html', {'error': 'Please, use a valid product name.'})
    
    return render(request, 'search_product.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            product_name = form.cleaned_data['name']
            product_exists = Product.objects.filter(name__iexact=product_name).first()

            if product_exists:
                product_exists.qty += form.cleaned_data['qty']
                product_exists.save()
                return render(request, 'add_product.html', {'message': 'Product updated.'})
            else:
                form.save()
                return render(request, 'add_product.html', {'message': 'Product included.'})
        else:
            print(f"Form errors in add_product: {form.errors}")
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('/')