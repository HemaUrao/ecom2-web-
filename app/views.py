from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Service, Contact, About, SinglePage, IndexPage


# Create your views here.

def IndexPage(request):
    return render(request, 'app/index.html')

def AboutPage(request):
    return render(request, 'app/about.html')

def ProductPage(request):
    
    return render(request, 'app/product.html')


def ServicesPage(request):          
    return render(request, 'app/services.html') 

def ContactPage(request):
    return render(request, 'app/contact.html')

def BasePage(request):
    return render(request, 'app/base.html')

def SinglePage(request):        
    return render(request, 'app/single.html')

from django.shortcuts import render
from .models import Product

def CartPage(request):
    cart_ids = request.session.get('cart', [])
    cart_items = []
    cart_subtotal = 0
    for pid in cart_ids:
        product = Product.objects.get(id=pid)
        item = {
            'product': product,
            'quantity': 1,  # or fetch quantity if you store it
            'id': product.id,
            'subtotal': product.price,
        }
        cart_items.append(item)
        cart_subtotal += product.price
    cart_total = cart_subtotal  # Add shipping/tax if needed
    return render(request, 'app/cart.html', {
        'cart': cart_items,
        'cart_subtotal': cart_subtotal,
        'cart_total': cart_total,
    })


def add_to_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', [])
        cart.append(product_id)
        request.session['cart'] = cart
        return HttpResponse(f"Product {product_id} added to cart.")
    else:
        return HttpResponse("Invalid request method.", status=405)


def product_detail(request, product_id):
    if request.method == 'GET':
        return HttpResponse(f"Details of product {product_id}.")
    return HttpResponse(f"Details of product {product_id}.")


    