from django.shortcuts import redirect, get_object_or_404
from .models import Order
from accounts.models import Account
from accounts.email_utils import send_order_status_email_to_user


def accept_order(request, id):
    if request.session.get('role') != 'farmer':
        return redirect('/login/')
    order = get_object_or_404(Order, id=id)
    order.status = 'accepted'
    order.save()
    try:
        customer = Account.objects.get(id=order.user_id)
        farmer = Account.objects.get(id=order.farmer_id)
        send_order_status_email_to_user(order, customer, farmer, 'accepted')
    except Account.DoesNotExist:
        pass
    return redirect('/pending-orders/')


def reject_order(request, id):
    if request.session.get('role') != 'farmer':
        return redirect('/login/')
    order = get_object_or_404(Order, id=id)
    order.status = 'rejected'
    order.save()
    try:
        customer = Account.objects.get(id=order.user_id)
        farmer = Account.objects.get(id=order.farmer_id)
        send_order_status_email_to_user(order, customer, farmer, 'rejected')
    except Account.DoesNotExist:
        pass
    return redirect('/pending-orders/')


def mark_out_for_delivery(request, id):
    if request.session.get('role') != 'farmer':
        return redirect('/login/')
    order = get_object_or_404(Order, id=id)
    order.status = 'out_for_delivery'
    order.save()
    return redirect('/accepted-orders/')


def mark_delivered(request, id):
    if request.session.get('role') != 'farmer':
        return redirect('/login/')
    order = get_object_or_404(Order, id=id)
    order.status = 'delivered'
    order.save()
    return redirect('/accepted-orders/')
