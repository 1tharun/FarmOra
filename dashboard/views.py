from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from orders.models import Order
from accounts.models import Account


def farmer_dashboard(request):
    if request.session.get("role") != "farmer":
        return redirect("/login/")
    farmer_id = request.session.get("user_id")
    products = Product.objects.filter(farmer_id=farmer_id)
    orders = Order.objects.filter(farmer_id=farmer_id).exclude(status="pending")
    total_orders = orders.count()
    total_earnings = sum(o.total for o in orders if o.status == "accepted")
    pending_count = Order.objects.filter(farmer_id=farmer_id, status="pending").count()
    return render(request, "farmer_dashboard.html", {
        "products": products,
        "orders": orders,
        "total_orders": total_orders,
        "total_earnings": total_earnings,
        "pending_count": pending_count,
    })


def add_product(request):
    if request.session.get("role") != "farmer":
        return redirect("/login/")
    if request.method == "POST":
        Product.objects.create(
            name=request.POST["name"],
            telugu_name=request.POST.get("telugu_name", ""),
            price=request.POST["price"],
            image=request.POST.get("image", ""),
            farmer_id=request.session.get("user_id")
        )
        return redirect("/farmer-dashboard/")
    return render(request, "add_product.html")


def edit_product(request, id):
    if request.session.get("role") != "farmer":
        return redirect("/login/")
    product = get_object_or_404(Product, id=id, farmer_id=request.session.get("user_id"))
    if request.method == "POST":
        product.name = request.POST["name"]
        product.telugu_name = request.POST.get("telugu_name", "")
        product.price = request.POST["price"]
        product.image = request.POST.get("image", "")
        product.save()
        return redirect("/farmer-dashboard/")
    return render(request, "edit_product.html", {"product": product})


def delete_product(request, id):
    if request.session.get("role") != "farmer":
        return redirect("/login/")
    product = get_object_or_404(Product, id=id, farmer_id=request.session.get("user_id"))
    if request.method == "POST":
        product.delete()
        return redirect("/farmer-dashboard/")
    return render(request, "delete_product.html", {"product": product})


def pending_orders(request):
    if request.session.get("role") != "farmer":
        return redirect("/login/")
    farmer_id = request.session.get("user_id")
    orders = Order.objects.filter(farmer_id=farmer_id, status="pending").order_by("-created_at")
    pending_count = orders.count()
    return render(request, "pending_orders.html", {
        "orders": orders,
        "pending_count": pending_count,
    })


def farmer_contact_directory(request):
    if not request.session.get('user_id'):
        return redirect('/login/')
    if request.session.get('role') != 'user':
        return redirect('/farmer-dashboard/')

    farmers = Account.objects.filter(role='farmer')
    farmer_data = []
    for farmer in farmers:
        product_count = Product.objects.filter(farmer_id=farmer.id).count()
        farmer_data.append({
            'farmer': farmer,
            'product_count': product_count,
        })

    return render(request, 'farmer_contact.html', {'farmer_data': farmer_data})
