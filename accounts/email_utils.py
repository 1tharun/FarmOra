from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_registration_email(user):
    """Send HTML welcome email on registration."""
    try:
        if user.role == 'farmer':
            subject = '🌾 Welcome to Farmora — Farmer Account Created!'
            html_content = f"""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="margin:0;padding:0;background:#f4f6f3;font-family:'Segoe UI',Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f6f3;padding:30px 0;">
    <tr><td align="center">
      <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <!-- Header -->
        <tr><td style="background:linear-gradient(135deg,#1c3a28,#2a5240);padding:40px 40px 30px;text-align:center;">
          <h1 style="color:#e8b860;font-size:36px;margin:0;letter-spacing:2px;">🌾 FARMORA</h1>
          <p style="color:rgba(255,255,255,0.75);margin:8px 0 0;font-size:14px;letter-spacing:1px;">FARMER PORTAL</p>
        </td></tr>
        <!-- Body -->
        <tr><td style="padding:40px;">
          <h2 style="color:#1c3a28;font-size:24px;margin:0 0 16px;">Welcome, {user.name}! 👋</h2>
          <p style="color:#4a4a4a;line-height:1.7;margin:0 0 24px;">Your farmer account has been successfully created on Farmora. You can now start listing your fresh produce and connect with customers directly.</p>
          <table width="100%" cellpadding="0" cellspacing="0" style="background:#f0f7f3;border-radius:8px;padding:20px;margin-bottom:24px;">
            <tr><td>
              <p style="margin:0 0 8px;font-weight:600;color:#1c3a28;">📋 Your Account Details:</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Name:</strong> {user.name}</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Email:</strong> {user.email}</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Mobile:</strong> {user.mobile_number or 'Not provided'}</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Role:</strong> Farmer 🌾</p>
            </td></tr>
          </table>
          <p style="color:#4a4a4a;font-weight:600;margin:0 0 12px;">🚀 What you can do:</p>
          <ul style="color:#4a4a4a;line-height:2;padding-left:20px;margin:0 0 28px;">
            <li>List your fresh produce for sale</li>
            <li>Receive order notifications by email</li>
            <li>Accept or reject customer orders</li>
            <li>Track your earnings on the dashboard</li>
            <li>Connect directly with customers</li>
          </ul>
          <div style="text-align:center;">
            <a href="http://127.0.0.1:8000/login/" style="display:inline-block;background:linear-gradient(135deg,#1c3a28,#2a5240);color:#e8b860;text-decoration:none;padding:14px 36px;border-radius:6px;font-weight:600;font-size:15px;letter-spacing:0.5px;">Login to Your Dashboard →</a>
          </div>
        </td></tr>
        <!-- Footer -->
        <tr><td style="background:#f0f7f3;padding:20px 40px;text-align:center;border-top:1px solid #dde8e0;">
          <p style="color:#7a7a7a;font-size:12px;margin:0;">© 2026 Farmora · Connecting Farmers & Customers · Hyderabad</p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>
"""
            plain_text = f"Hi {user.name},\n\nWelcome to Farmora! Your farmer account has been successfully created.\n\nYou can now log in and start listing your fresh produce.\n\nLogin: http://127.0.0.1:8000/login/\n\nHappy selling!\nFarmora Team"
        else:
            subject = '🛒 Welcome to Farmora — Shop Fresh Produce Directly from Farmers!'
            html_content = f"""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="margin:0;padding:0;background:#f4f6f3;font-family:'Segoe UI',Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f6f3;padding:30px 0;">
    <tr><td align="center">
      <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <!-- Header -->
        <tr><td style="background:linear-gradient(135deg,#1c3a28,#2a5240);padding:40px 40px 30px;text-align:center;">
          <h1 style="color:#e8b860;font-size:36px;margin:0;letter-spacing:2px;">🛒 FARMORA</h1>
          <p style="color:rgba(255,255,255,0.75);margin:8px 0 0;font-size:14px;letter-spacing:1px;">CUSTOMER PORTAL</p>
        </td></tr>
        <!-- Body -->
        <tr><td style="padding:40px;">
          <h2 style="color:#1c3a28;font-size:24px;margin:0 0 16px;">Welcome, {user.name}! 👋</h2>
          <p style="color:#4a4a4a;line-height:1.7;margin:0 0 24px;">Your Farmora account is ready! You can now browse and order fresh produce directly from local farmers in your area.</p>
          <table width="100%" cellpadding="0" cellspacing="0" style="background:#f0f7f3;border-radius:8px;padding:20px;margin-bottom:24px;">
            <tr><td>
              <p style="margin:0 0 8px;font-weight:600;color:#1c3a28;">📋 Your Account Details:</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Name:</strong> {user.name}</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Email:</strong> {user.email}</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Mobile:</strong> {user.mobile_number or 'Not provided'}</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Role:</strong> Customer 🛍️</p>
            </td></tr>
          </table>
          <p style="color:#4a4a4a;font-weight:600;margin:0 0 12px;">🚀 What you can do:</p>
          <ul style="color:#4a4a4a;line-height:2;padding-left:20px;margin:0 0 28px;">
            <li>Browse fresh produce from local farmers</li>
            <li>Add items to cart and place orders</li>
            <li>Get email updates when farmer accepts your order</li>
            <li>Browse the farmer directory to contact farmers directly</li>
            <li>Track your order history</li>
          </ul>
          <div style="text-align:center;">
            <a href="http://127.0.0.1:8000/login/" style="display:inline-block;background:linear-gradient(135deg,#1c3a28,#2a5240);color:#e8b860;text-decoration:none;padding:14px 36px;border-radius:6px;font-weight:600;font-size:15px;letter-spacing:0.5px;">Start Shopping →</a>
          </div>
        </td></tr>
        <!-- Footer -->
        <tr><td style="background:#f0f7f3;padding:20px 40px;text-align:center;border-top:1px solid #dde8e0;">
          <p style="color:#7a7a7a;font-size:12px;margin:0;">© 2026 Farmora · Connecting Farmers & Customers · Hyderabad</p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>
"""
            plain_text = f"Hi {user.name},\n\nWelcome to Farmora! Your account has been successfully created.\n\nBrowse fresh produce directly from local farmers and place orders.\n\nLogin: http://127.0.0.1:8000/login/\n\nHappy shopping!\nFarmora Team"

        msg = EmailMultiAlternatives(
            subject=subject,
            body=plain_text,
           from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    except Exception as e:
        print(f'[Farmora] Registration email error: {e}')
        return False


def send_order_notification_to_farmer(order, farmer, customer):
    """Send order notification email to farmer when customer places order."""
    try:
        subject = f'📦 New Order for {order.product.name} - Action Required'
        html_content = f"""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="margin:0;padding:0;background:#f4f6f3;font-family:'Segoe UI',Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f6f3;padding:30px 0;">
    <tr><td align="center">
      <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <tr><td style="background:linear-gradient(135deg,#1c3a28,#2a5240);padding:35px 40px;text-align:center;">
          <h1 style="color:#e8b860;font-size:30px;margin:0;">📦 New Order Received!</h1>
          <p style="color:rgba(255,255,255,0.75);margin:8px 0 0;font-size:14px;">Action required — please accept or reject</p>
        </td></tr>
        <tr><td style="padding:40px;">
          <p style="color:#4a4a4a;line-height:1.7;margin:0 0 24px;">Hi <strong>{farmer.name}</strong>, you have a new order waiting for your response!</p>
          <!-- Order Details -->
          <table width="100%" cellpadding="0" cellspacing="0" style="background:#f0f7f3;border-radius:8px;padding:20px;margin-bottom:20px;border-left:4px solid #2a5240;">
            <tr><td>
              <p style="margin:0 0 12px;font-weight:700;color:#1c3a28;font-size:15px;">📋 Order Details</p>
              <table width="100%">
                <tr><td style="color:#666;font-size:13px;padding:4px 0;width:40%;">Order ID</td><td style="color:#1c3a28;font-weight:600;font-size:13px;">#{order.id}</td></tr>
                <tr><td style="color:#666;font-size:13px;padding:4px 0;">Product</td><td style="color:#1c3a28;font-weight:600;font-size:13px;">{order.product.name}</td></tr>
                <tr><td style="color:#666;font-size:13px;padding:4px 0;">Quantity</td><td style="color:#1c3a28;font-weight:600;font-size:13px;">{order.quantity} unit(s)</td></tr>
                <tr><td style="color:#666;font-size:13px;padding:4px 0;">Price per unit</td><td style="color:#1c3a28;font-weight:600;font-size:13px;">₹{order.product.price}</td></tr>
                <tr><td style="color:#666;font-size:13px;padding:4px 0;">Total Amount</td><td style="color:#e8b860;font-weight:700;font-size:15px;">₹{order.total}</td></tr>
                <tr><td style="color:#666;font-size:13px;padding:4px 0;">Order Date</td><td style="color:#1c3a28;font-weight:600;font-size:13px;">{order.created_at.strftime('%d %b %Y, %I:%M %p')}</td></tr>
              </table>
            </td></tr>
          </table>
          <!-- Customer Details -->
          <table width="100%" cellpadding="0" cellspacing="0" style="background:#fff8ee;border-radius:8px;padding:20px;margin-bottom:24px;border-left:4px solid #e8b860;">
            <tr><td>
              <p style="margin:0 0 12px;font-weight:700;color:#7a5000;font-size:15px;">👤 Customer Details</p>
              <table width="100%">
                <tr><td style="color:#666;font-size:13px;padding:4px 0;width:40%;">Name</td><td style="color:#1c3a28;font-weight:600;font-size:13px;">{customer.name}</td></tr>
                <tr><td style="color:#666;font-size:13px;padding:4px 0;">Email</td><td style="font-size:13px;"><a href="mailto:{customer.email}" style="color:#2a5240;font-weight:600;">{customer.email}</a></td></tr>
                <tr><td style="color:#666;font-size:13px;padding:4px 0;">Phone</td><td style="font-size:13px;"><a href="tel:{customer.mobile_number}" style="color:#2a5240;font-weight:700;font-size:14px;">📞 {customer.mobile_number or 'Not provided'}</a></td></tr>
                <tr><td style="color:#666;font-size:13px;padding:4px 0;vertical-align:top;">Delivery Address</td><td style="color:#1c3a28;font-size:13px;">{customer.address or 'Not provided'}</td></tr>
              </table>
            </td></tr>
          </table>
          <div style="text-align:center;">
            <a href="http://127.0.0.1:8000/pending-orders/" style="display:inline-block;background:linear-gradient(135deg,#1c3a28,#2a5240);color:#e8b860;text-decoration:none;padding:14px 36px;border-radius:6px;font-weight:600;font-size:15px;">View Pending Orders →</a>
          </div>
        </td></tr>
        <tr><td style="background:#f0f7f3;padding:20px 40px;text-align:center;border-top:1px solid #dde8e0;">
          <p style="color:#7a7a7a;font-size:12px;margin:0;">© 2026 Farmora · Connecting Farmers & Customers</p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>
"""
        plain_text = f"""Hi {farmer.name},

New Order Received! (Order #{order.id})

PRODUCT: {order.product.name}
QUANTITY: {order.quantity}
TOTAL: Rs.{order.total}

CUSTOMER: {customer.name}
PHONE: {customer.mobile_number or 'Not provided'}
EMAIL: {customer.email}
ADDRESS: {customer.address or 'Not provided'}

Login to accept or reject: http://127.0.0.1:8000/pending-orders/

Farmora Team"""

        msg = EmailMultiAlternatives(
            subject=subject,
            body=plain_text,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[farmer.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    except Exception as e:
        print(f'[Farmora] Order notification email error: {e}')
        return False


def send_order_status_email_to_user(order, customer, farmer, status):
    """Send order status (accepted/rejected) email to customer."""
    try:
        if status == 'accepted':
            subject = f'✅ Your Order #{order.id} Has Been Accepted!'
            header_bg = 'linear-gradient(135deg,#1c4d2a,#2a6240)'
            header_icon = '✅'
            header_title = 'Order Accepted!'
            header_sub = 'Great news — your order is confirmed'
            status_color = '#1c4d2a'
            status_bg = '#e8f5e9'
            status_border = '#4CAF50'
            status_label = 'ACCEPTED'
            next_steps_html = f"""
              <li>Contact the farmer to confirm delivery time</li>
              <li>Keep your delivery address ready</li>
              <li>Arrange payment with the farmer directly</li>
              <li>Expect fresh produce soon! 🥬</li>
"""
        else:
            subject = f'❌ Your Order #{order.id} Has Been Declined'
            header_bg = 'linear-gradient(135deg,#4d1c1c,#6b2626)'
            header_icon = '❌'
            header_title = 'Order Declined'
            header_sub = 'Sorry — the farmer could not fulfil this order'
            status_color = '#7a1c1c'
            status_bg = '#fdecea'
            status_border = '#e53935'
            status_label = 'DECLINED'
            next_steps_html = """
              <li>Browse other farmers on the shop page</li>
              <li>Try placing a new order with a different farmer</li>
              <li>Check the Farmer Directory to contact farmers directly</li>
"""

        html_content = f"""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="margin:0;padding:0;background:#f4f6f3;font-family:'Segoe UI',Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f6f3;padding:30px 0;">
    <tr><td align="center">
      <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.08);">
        <tr><td style="background:{header_bg};padding:35px 40px;text-align:center;">
          <h1 style="color:#ffffff;font-size:30px;margin:0;">{header_icon} {header_title}</h1>
          <p style="color:rgba(255,255,255,0.8);margin:8px 0 0;font-size:14px;">{header_sub}</p>
        </td></tr>
        <tr><td style="padding:40px;">
          <p style="color:#4a4a4a;line-height:1.7;margin:0 0 20px;">Hi <strong>{customer.name}</strong>,</p>
          <!-- Status Badge -->
          <table width="100%" cellpadding="0" cellspacing="0" style="background:{status_bg};border-radius:8px;padding:16px 20px;margin-bottom:20px;border-left:4px solid {status_border};">
            <tr><td>
              <p style="margin:0;color:{status_color};font-weight:700;font-size:16px;">Order #{order.id} — <span>{status_label}</span></p>
            </td></tr>
          </table>
          <!-- Order Summary -->
          <table width="100%" cellpadding="0" cellspacing="0" style="background:#f0f7f3;border-radius:8px;padding:20px;margin-bottom:20px;border-left:4px solid #2a5240;">
            <tr><td>
              <p style="margin:0 0 12px;font-weight:700;color:#1c3a28;font-size:15px;">📋 Order Summary</p>
              <table width="100%">
                <tr><td style="color:#666;font-size:13px;padding:4px 0;width:40%;">Product</td><td style="color:#1c3a28;font-weight:600;font-size:13px;">{order.product.name}</td></tr>
                <tr><td style="color:#666;font-size:13px;padding:4px 0;">Quantity</td><td style="color:#1c3a28;font-weight:600;font-size:13px;">{order.quantity} unit(s)</td></tr>
                <tr><td style="color:#666;font-size:13px;padding:4px 0;">Total</td><td style="color:#e8b860;font-weight:700;font-size:15px;">₹{order.total}</td></tr>
              </table>
            </td></tr>
          </table>
          <!-- Farmer Contact -->
          <table width="100%" cellpadding="0" cellspacing="0" style="background:#fff8ee;border-radius:8px;padding:20px;margin-bottom:24px;border-left:4px solid #e8b860;">
            <tr><td>
              <p style="margin:0 0 12px;font-weight:700;color:#7a5000;font-size:15px;">🌾 Farmer Contact</p>
              <table width="100%">
                <tr><td style="color:#666;font-size:13px;padding:4px 0;width:40%;">Farmer</td><td style="color:#1c3a28;font-weight:600;font-size:13px;">{farmer.name}</td></tr>
                <tr><td style="color:#666;font-size:13px;padding:4px 0;">Phone</td><td style="font-size:13px;"><a href="tel:{farmer.mobile_number}" style="color:#2a5240;font-weight:700;">📞 {farmer.mobile_number or 'Not provided'}</a></td></tr>
                <tr><td style="color:#666;font-size:13px;padding:4px 0;">Email</td><td style="font-size:13px;"><a href="mailto:{farmer.email}" style="color:#2a5240;font-weight:600;">{farmer.email}</a></td></tr>
              </table>
            </td></tr>
          </table>
          <!-- Next Steps -->
          <p style="font-weight:700;color:#1c3a28;margin:0 0 10px;">📌 Next Steps:</p>
          <ul style="color:#4a4a4a;line-height:2;padding-left:20px;margin:0 0 28px;">
            {next_steps_html}
          </ul>
          <div style="text-align:center;">
            <a href="http://127.0.0.1:8000/shop/" style="display:inline-block;background:linear-gradient(135deg,#1c3a28,#2a5240);color:#e8b860;text-decoration:none;padding:14px 36px;border-radius:6px;font-weight:600;font-size:15px;">Continue Shopping →</a>
          </div>
        </td></tr>
        <tr><td style="background:#f0f7f3;padding:20px 40px;text-align:center;border-top:1px solid #dde8e0;">
          <p style="color:#7a7a7a;font-size:12px;margin:0;">© 2026 Farmora · Connecting Farmers & Customers</p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>
"""
        plain_text = f"""Hi {customer.name},

Your Order #{order.id} has been {status.upper()}.

Product: {order.product.name}
Quantity: {order.quantity}
Total: Rs.{order.total}

Farmer: {farmer.name}
Farmer Phone: {farmer.mobile_number or 'Not provided'}
Farmer Email: {farmer.email}

Continue Shopping: http://127.0.0.1:8000/shop/

Farmora Team"""

        msg = EmailMultiAlternatives(
            subject=subject,
            body=plain_text,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[customer.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    except Exception as e:
        print(f'[Farmora] Order status email error: {e}')
        return False
