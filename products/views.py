from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from orders.models import Order
from accounts.models import Account
from accounts.email_utils import send_order_notification_to_farmer


def shop(request):
    if not request.session.get('user_id'):
        return redirect('/login/')
    q = request.GET.get('q', '').strip()
    products = Product.objects.all()
    if q:
        products = products.filter(name__icontains=q) | products.filter(telugu_name__icontains=q)
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())
    return render(request, 'shop.html', {
        'products': products,
        'cart': cart,
        'cart_count': cart_count,
        'q': q,
    })


def add_to_cart(request, id):
    if not request.session.get('user_id'):
        return redirect('/login/')
    cart = request.session.get('cart', {})
    key = str(id)
    cart[key] = cart.get(key, 0) + 1
    request.session['cart'] = cart
    return redirect('/shop/')


def decrease_cart(request, id):
    if not request.session.get('user_id'):
        return redirect('/login/')
    cart = request.session.get('cart', {})
    key = str(id)
    if key in cart:
        cart[key] -= 1
        if cart[key] <= 0:
            del cart[key]
    request.session['cart'] = cart
    return redirect('/shop/')


def remove_from_cart(request, id):
    if not request.session.get('user_id'):
        return redirect('/login/')
    cart = request.session.get('cart', {})
    key = str(id)
    if key in cart:
        del cart[key]
    request.session['cart'] = cart
    return redirect('/cart/')


def cart_view(request):
    if not request.session.get('user_id'):
        return redirect('/login/')
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for product_id, qty in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))
            subtotal = product.price * qty
            total += subtotal
            items.append({'product': product, 'qty': qty, 'subtotal': subtotal})
        except Product.DoesNotExist:
            pass
    return render(request, 'cart.html', {'items': items, 'total': total})


def place_order(request):
    if not request.session.get('user_id'):
        return redirect('/login/')
    cart = request.session.get('cart', {})
    user_id = request.session.get('user_id')

    try:
        customer = Account.objects.get(id=user_id)
    except Account.DoesNotExist:
        return redirect('/login/')

    for product_id, qty in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))
            order = Order.objects.create(
                user_id=user_id,
                farmer_id=product.farmer_id,
                product=product,
                quantity=qty,
                total=product.price * qty,
                status='pending',
            )
            # Send email notification to farmer
            try:
                farmer = Account.objects.get(id=product.farmer_id)
                send_order_notification_to_farmer(order, farmer, customer)
            except Account.DoesNotExist:
                pass
        except Product.DoesNotExist:
            pass

    request.session['cart'] = {}
    return redirect('/orders/')


def order_history(request):
    if not request.session.get('user_id'):
        return redirect('/login/')
    user_id = request.session.get('user_id')
    orders = Order.objects.filter(user_id=user_id).order_by('-created_at')
    return render(request, 'order_history.html', {'orders': orders})
