from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def search_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name', '').strip()
        # print(f"Received product_name in search_product: '{product_name}'")

        if product_name:
            product = Product.objects.filter(name__icontains=product_name).first()
            # print(f"Found product in search_product: {product}")

            if product:
                return render(request, 'product_exists.html', {'product': product})
            else:
                form = ProductForm(initial={'name': product_name})
                return redirect('add_product')
        else: 
            return render(request, 'search_product.html', {'error': 'Please, use a valid product name.'})
    
    return render(request, 'search_product.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        # print(f"Form data in add_product: {request.POST}")

        if form.is_valid():
            product_name = form.cleaned_data['name']
            product_exists = Product.objects.filter(name__iexact=product_name).first()
            # print(f"Product exists in add_product: {product_exists}")

            if product_exists:
                product_exists.qty += form.cleaned_data['qty']
                product_exists.save()
                return redirect('search_product')
            else:
                form.save()
                return redirect('search_product')
        else:
            print(f"Form errors in add_product: {form.errors}")
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})