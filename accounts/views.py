from django.shortcuts import render, redirect
from .models import Account
from .email_utils import send_registration_email


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
            name=name,
            email=email,
            password=password,
            role=role,
            mobile_number=mobile_number,
            address=address,
        )

        try:
            send_registration_email(user)
        except Exception as e:
            import traceback
            print(f'[Farmora] Registration email error: {e}')
            print(traceback.format_exc())
        return False
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
