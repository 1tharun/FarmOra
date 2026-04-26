import os
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

SITE_URL = 'https://farmora-production.up.railway.app'
FROM_EMAIL = 'farmora.farmer@gmail.com'
FROM_NAME = 'Farmora'


def get_api():
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = os.environ.get('BREVO_API_KEY', '')
    return sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))


def send_registration_email(user):
    try:
        api = get_api()

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
        <tr><td style="background:linear-gradient(135deg,#1c3a28,#2a5240);padding:40px;text-align:center;">
          <h1 style="color:#e8b860;font-size:36px;margin:0;">🌾 FARMORA</h1>
          <p style="color:rgba(255,255,255,0.75);margin:8px 0 0;font-size:14px;">FARMER PORTAL</p>
        </td></tr>
        <tr><td style="padding:40px;">
          <h2 style="color:#1c3a28;">Welcome, {user.name}! 👋</h2>
          <p style="color:#4a4a4a;line-height:1.7;">Your farmer account has been successfully created on Farmora.</p>
          <table width="100%" style="background:#f0f7f3;border-radius:8px;padding:20px;margin-bottom:24px;">
            <tr><td>
              <p style="margin:0 0 8px;font-weight:600;color:#1c3a28;">📋 Your Account Details:</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Name:</strong> {user.name}</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Email:</strong> {user.email}</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Mobile:</strong> {user.mobile_number or 'Not provided'}</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Role:</strong> Farmer 🌾</p>
            </td></tr>
          </table>
          <p style="color:#4a4a4a;font-weight:600;">🚀 What you can do:</p>
          <ul style="color:#4a4a4a;line-height:2;">
            <li>List your fresh produce for sale</li>
            <li>Receive order notifications by email</li>
            <li>Accept or reject customer orders</li>
            <li>Connect directly with customers</li>
          </ul>
          <div style="text-align:center;margin-top:24px;">
            <a href="{SITE_URL}/login/" style="background:linear-gradient(135deg,#1c3a28,#2a5240);color:#e8b860;text-decoration:none;padding:14px 36px;border-radius:6px;font-weight:600;">Login to Dashboard →</a>
          </div>
        </td></tr>
        <tr><td style="background:#f0f7f3;padding:20px;text-align:center;">
          <p style="color:#7a7a7a;font-size:12px;margin:0;">© 2026 Farmora · Hyderabad</p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>
"""
        else:
            subject = '🛒 Welcome to Farmora — Shop Fresh Produce!'
            html_content = f"""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="margin:0;padding:0;background:#f4f6f3;font-family:'Segoe UI',Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f6f3;padding:30px 0;">
    <tr><td align="center">
      <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:12px;overflow:hidden;">
        <tr><td style="background:linear-gradient(135deg,#1c3a28,#2a5240);padding:40px;text-align:center;">
          <h1 style="color:#e8b860;font-size:36px;margin:0;">🛒 FARMORA</h1>
          <p style="color:rgba(255,255,255,0.75);margin:8px 0 0;font-size:14px;">CUSTOMER PORTAL</p>
        </td></tr>
        <tr><td style="padding:40px;">
          <h2 style="color:#1c3a28;">Welcome, {user.name}! 👋</h2>
          <p style="color:#4a4a4a;line-height:1.7;">Your Farmora account is ready! Browse fresh produce directly from local farmers.</p>
          <table width="100%" style="background:#f0f7f3;border-radius:8px;padding:20px;margin-bottom:24px;">
            <tr><td>
              <p style="margin:0 0 8px;font-weight:600;color:#1c3a28;">📋 Your Account Details:</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Name:</strong> {user.name}</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Email:</strong> {user.email}</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Mobile:</strong> {user.mobile_number or 'Not provided'}</p>
              <p style="margin:4px 0;color:#4a4a4a;font-size:14px;"><strong>Role:</strong> Customer 🛍️</p>
            </td></tr>
          </table>
          <p style="color:#4a4a4a;font-weight:600;">🚀 What you can do:</p>
          <ul style="color:#4a4a4a;line-height:2;">
            <li>Browse fresh produce from local farmers</li>
            <li>Add items to cart and place orders</li>
            <li>Track your orders in real time</li>
            <li>Rate and review products</li>
          </ul>
          <div style="text-align:center;margin-top:24px;">
            <a href="{SITE_URL}/shop/" style="background:linear-gradient(135deg,#1c3a28,#2a5240);color:#e8b860;text-decoration:none;padding:14px 36px;border-radius:6px;font-weight:600;">Start Shopping →</a>
          </div>
        </td></tr>
        <tr><td style="background:#f0f7f3;padding:20px;text-align:center;">
          <p style="color:#7a7a7a;font-size:12px;margin:0;">© 2026 Farmora · Hyderabad</p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>
"""

        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=[{"email": user.email, "name": user.name}],
            sender={"email": FROM_EMAIL, "name": FROM_NAME},
            subject=subject,
            html_content=html_content,
        )
        api.send_transac_email(send_smtp_email)
        print(f'[Farmora] Registration email sent to {user.email}')
        return True
    except ApiException as e:
        print(f'[Farmora] Brevo API error: {e}')
        return False
    except Exception as e:
        print(f'[Farmora] Registration email error: {e}')
        return False


def send_order_notification_to_farmer(order, farmer, customer):
    try:
        api = get_api()
        subject = f'📦 New Order for {order.product.name} - Action Required'
        html_content = f"""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="margin:0;padding:0;background:#f4f6f3;font-family:'Segoe UI',Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f6f3;padding:30px 0;">
    <tr><td align="center">
      <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:12px;overflow:hidden;">
        <tr><td style="background:linear-gradient(135deg,#1c3a28,#2a5240);padding:35px 40px;text-align:center;">
          <h1 style="color:#e8b860;font-size:30px;margin:0;">📦 New Order Received!</h1>
          <p style="color:rgba(255,255,255,0.75);margin:8px 0 0;">Action required — please accept or reject</p>
        </td></tr>
        <tr><td style="padding:40px;">
          <p style="color:#4a4a4a;">Hi <strong>{farmer.name}</strong>, you have a new order!</p>
          <table width="100%" style="background:#f0f7f3;border-radius:8px;padding:20px;margin-bottom:20px;">
            <tr><td>
              <p style="font-weight:700;color:#1c3a28;">📋 Order Details</p>
              <p style="color:#4a4a4a;font-size:14px;"><strong>Order ID:</strong> #{order.id}</p>
              <p style="color:#4a4a4a;font-size:14px;"><strong>Product:</strong> {order.product.name}</p>
              <p style="color:#4a4a4a;font-size:14px;"><strong>Quantity:</strong> {order.quantity}</p>
              <p style="color:#e8b860;font-size:16px;font-weight:700;"><strong>Total:</strong> ₹{order.total}</p>
            </td></tr>
          </table>
          <table width="100%" style="background:#fff8ee;border-radius:8px;padding:20px;margin-bottom:24px;">
            <tr><td>
              <p style="font-weight:700;color:#7a5000;">👤 Customer Details</p>
              <p style="color:#4a4a4a;font-size:14px;"><strong>Name:</strong> {customer.name}</p>
              <p style="color:#4a4a4a;font-size:14px;"><strong>Phone:</strong> <a href="tel:{customer.mobile_number}" style="color:#2a5240;">📞 {customer.mobile_number or 'Not provided'}</a></p>
              <p style="color:#4a4a4a;font-size:14px;"><strong>Email:</strong> {customer.email}</p>
              <p style="color:#4a4a4a;font-size:14px;"><strong>Address:</strong> {customer.address or 'Not provided'}</p>
            </td></tr>
          </table>
          <div style="text-align:center;">
            <a href="{SITE_URL}/pending-orders/" style="background:linear-gradient(135deg,#1c3a28,#2a5240);color:#e8b860;text-decoration:none;padding:14px 36px;border-radius:6px;font-weight:600;">View Pending Orders →</a>
          </div>
        </td></tr>
        <tr><td style="background:#f0f7f3;padding:20px;text-align:center;">
          <p style="color:#7a7a7a;font-size:12px;margin:0;">© 2026 Farmora · Hyderabad</p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>
"""
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=[{"email": farmer.email, "name": farmer.name}],
            sender={"email": FROM_EMAIL, "name": FROM_NAME},
            subject=subject,
            html_content=html_content,
        )
        api.send_transac_email(send_smtp_email)
        print(f'[Farmora] Order notification sent to {farmer.email}')
        return True
    except ApiException as e:
        print(f'[Farmora] Brevo API error: {e}')
        return False
    except Exception as e:
        print(f'[Farmora] Order notification error: {e}')
        return False


def send_order_status_email_to_user(order, customer, farmer, status):
    try:
        api = get_api()

        if status == 'accepted':
            subject = f'✅ Your Order #{order.id} Has Been Accepted!'
            status_color = '#1c4d2a'
            status_bg = '#e8f5e9'
            status_label = '✅ ACCEPTED'
            next_steps = """
                <li>Contact the farmer to confirm delivery time</li>
                <li>Keep your delivery address ready</li>
                <li>Arrange payment with the farmer directly</li>
                <li>Expect fresh produce soon! 🥬</li>
"""
        else:
            subject = f'❌ Your Order #{order.id} Has Been Declined'
            status_color = '#7a1c1c'
            status_bg = '#fdecea'
            status_label = '❌ DECLINED'
            next_steps = """
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
      <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:12px;overflow:hidden;">
        <tr><td style="background:{status_color};padding:35px 40px;text-align:center;">
          <h1 style="color:#ffffff;font-size:28px;margin:0;">{status_label}</h1>
          <p style="color:rgba(255,255,255,0.8);margin:8px 0 0;">Order #{order.id} update</p>
        </td></tr>
        <tr><td style="padding:40px;">
          <p style="color:#4a4a4a;">Hi <strong>{customer.name}</strong>,</p>
          <table width="100%" style="background:{status_bg};border-radius:8px;padding:20px;margin-bottom:20px;">
            <tr><td>
              <p style="color:#4a4a4a;font-size:14px;"><strong>Product:</strong> {order.product.name}</p>
              <p style="color:#4a4a4a;font-size:14px;"><strong>Quantity:</strong> {order.quantity}</p>
              <p style="color:#4a4a4a;font-size:16px;font-weight:700;"><strong>Total:</strong> ₹{order.total}</p>
            </td></tr>
          </table>
          <table width="100%" style="background:#fff8ee;border-radius:8px;padding:20px;margin-bottom:24px;">
            <tr><td>
              <p style="font-weight:700;color:#7a5000;">🌾 Farmer Contact</p>
              <p style="color:#4a4a4a;font-size:14px;"><strong>Name:</strong> {farmer.name}</p>
              <p style="color:#4a4a4a;font-size:14px;"><strong>Phone:</strong> <a href="tel:{farmer.mobile_number}" style="color:#2a5240;">📞 {farmer.mobile_number or 'Not provided'}</a></p>
              <p style="color:#4a4a4a;font-size:14px;"><strong>Email:</strong> {farmer.email}</p>
            </td></tr>
          </table>
          <p style="font-weight:700;color:#1c3a28;">📌 Next Steps:</p>
          <ul style="color:#4a4a4a;line-height:2;">
            {next_steps}
          </ul>
          <div style="text-align:center;margin-top:24px;">
            <a href="{SITE_URL}/shop/" style="background:linear-gradient(135deg,#1c3a28,#2a5240);color:#e8b860;text-decoration:none;padding:14px 36px;border-radius:6px;font-weight:600;">Continue Shopping →</a>
          </div>
        </td></tr>
        <tr><td style="background:#f0f7f3;padding:20px;text-align:center;">
          <p style="color:#7a7a7a;font-size:12px;margin:0;">© 2026 Farmora · Hyderabad</p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>
"""
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=[{"email": customer.email, "name": customer.name}],
            sender={"email": FROM_EMAIL, "name": FROM_NAME},
            subject=subject,
            html_content=html_content,
        )
        api.send_transac_email(send_smtp_email)
        print(f'[Farmora] Order status email sent to {customer.email}')
        return True
    except ApiException as e:
        print(f'[Farmora] Brevo API error: {e}')
        return False
    except Exception as e:
        print(f'[Farmora] Order status email error: {e}')
        return False