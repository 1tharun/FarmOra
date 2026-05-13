from django.shortcuts import render, redirect
from .models import Account
from .email_utils import send_registration_email
import threading


def send_email_async(user):
    try:
        send_registration_email(user)
    except Exception as e:
        print(f'Email failed: {e}')


def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        mobile_number = request.POST.get('mobile_number', '')
        address = request.POST.get('address', '')

        if Account.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'An account with this email already exists.'})

        user = Account.objects.create(
            name=name, email=email, password=password,
            role=role, mobile_number=mobile_number, address=address,
        )

        thread = threading.Thread(target=send_email_async, args=(user,))
        thread.daemon = True
        thread.start()

        return redirect('/login/')

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = Account.objects.get(email=email, password=password)
            request.session['user_id'] = user.id
            request.session['role'] = user.role
            request.session['user_name'] = user.name
            request.session['cart'] = {}
            if user.role == "farmer":
                return redirect('/farmer-dashboard/')
            else:
                return redirect('/shop/')
        except Account.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
    return render(request, 'login.html')


def logout_view(request):
    request.session.flush()
    return redirect('/login/')


def profile_view(request):
    if not request.session.get('user_id'):
        return redirect('/login/')
    user = Account.objects.get(id=request.session['user_id'])
    return render(request, 'profile.html', {'user': user})


def edit_profile(request):
    if not request.session.get('user_id'):
        return redirect('/login/')
    user = Account.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        user.name = request.POST.get('name', user.name)
        user.mobile_number = request.POST.get('mobile_number', user.mobile_number)
        user.address = request.POST.get('address', user.address)
        user.save()
        request.session['user_name'] = user.name
        return redirect('/profile/')
    return render(request, 'edit_profile.html', {'user': user})