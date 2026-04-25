from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from .models import Product, Review
from orders.models import Order
from accounts.models import Account
from accounts.email_utils import send_order_notification_to_farmer


def shop(request):
    if not request.session.get('user_id'):
        return redirect('/login/')

    q = request.GET.get('q', '').strip()
    min_price = request.GET.get('min_price', '').strip()
    max_price = request.GET.get('max_price', '').strip()
    location = request.GET.get('location', '').strip()

    products = Product.objects.all()

    if q:
        products = products.filter(name__icontains=q) | products.filter(telugu_name__icontains=q)

    if min_price:
        try:
            products = products.filter(price__gte=float(min_price))
        except ValueError:
            pass

    if max_price:
        try:
            products = products.filter(price__lte=float(max_price))
        except ValueError:
            pass

    if location:
        # Filter by farmer address
        farmer_ids = Account.objects.filter(
            role='farmer', address__icontains=location
        ).values_list('id', flat=True)
        products = products.filter(farmer_id__in=farmer_ids)

    # Annotate with average rating
    products_with_data = []
    for product in products:
        avg_rating = product.reviews.aggregate(Avg('rating'))['rating__avg']
        review_count = product.reviews.count()
        farmer_name = ''
        farmer_location = ''
        try:
            farmer = Account.objects.get(id=product.farmer_id)
            farmer_name = farmer.name
            farmer_location = farmer.address or ''
        except Account.DoesNotExist:
            pass
        products_with_data.append({
            'product': product,
            'avg_rating': round(avg_rating, 1) if avg_rating else None,
            'review_count': review_count,
            'farmer_name': farmer_name,
            'farmer_location': farmer_location,
        })

    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())

    return render(request, 'shop.html', {
        'products_with_data': products_with_data,
        'cart': cart,
        'cart_count': cart_count,
        'q': q,
        'min_price': min_price,
        'max_price': max_price,
        'location': location,
        'total_count': len(products_with_data),
    })


def product_detail(request, id):
    if not request.session.get('user_id'):
        return redirect('/login/')

    product = get_object_or_404(Product, id=id)
    reviews = product.reviews.order_by('-created_at')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    user_id = request.session.get('user_id')

    # Check if user has ordered this product and it was accepted
    has_ordered = Order.objects.filter(
        user_id=user_id,
        product=product,
        status__in=['accepted', 'out_for_delivery', 'delivered']
    ).exists()

    # Check if user already reviewed
    already_reviewed = Review.objects.filter(product=product, user_id=user_id).exists()

    farmer_name = ''
    try:
        farmer = Account.objects.get(id=product.farmer_id)
        farmer_name = farmer.name
    except Account.DoesNotExist:
        pass

    if request.method == 'POST' and has_ordered and not already_reviewed:
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '')
        user_name = request.session.get('user_name', 'Customer')
        if rating:
            Review.objects.create(
                product=product,
                user_id=user_id,
                user_name=user_name,
                rating=int(rating),
                comment=comment,
            )
            return redirect(f'/product/{id}/')

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews,
        'avg_rating': round(avg_rating, 1) if avg_rating else None,
        'has_ordered': has_ordered,
        'already_reviewed': already_reviewed,
        'farmer_name': farmer_name,
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
