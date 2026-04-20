🌾 Farmora — Farm to Home, Fresh Every Day
A Django-based e-commerce platform connecting local farmers directly with customers. Built with simplicity, speed, and real communication in mind.

🚀 Live Demo

Deployed on Railway: https://farmora-production.up.railway.app


📦 Features

Farmer Registration — Farmers sign up and list their fresh produce
Customer Registration — Customers browse and order directly from farmers
Email Notifications — Beautiful HTML emails sent automatically:

Welcome email on registration (role-specific)
Order notification to farmer when customer places order
Order accepted / rejected email to customer


Farmer Directory — Customers can browse all farmers, call or email them directly
Cart System — Add, remove, increase/decrease items
Order Management — Farmers accept or reject pending orders
Farmer Dashboard — Track products, orders, and earnings
Mobile Numbers — Clickable tel: links for direct calling
Responsive Design — Works on mobile and desktop


🛠️ Tech Stack
LayerTechnologyBackendDjango 5.0DatabaseSQLite3 (local) / PostgreSQL (production)FrontendHTML, CSS (custom, no frameworks)EmailGmail SMTPHostingRailwayStatic FilesWhiteNoise

📁 Project Structure
farmora/
├── accounts/           # Registration, login, logout, email utils
│   ├── models.py       # Account model (name, email, mobile, address, role)
│   ├── views.py        # Register, login, logout views
│   └── email_utils.py  # All HTML email functions
├── products/           # Product listing, cart, orders
│   ├── models.py       # Product model
│   └── views.py        # Shop, cart, place order
├── orders/             # Order accept/reject
│   ├── models.py       # Order model
│   └── views.py        # Accept, reject views
├── dashboard/          # Farmer dashboard, farmer directory
│   └── views.py        # Dashboard, add/edit/delete product, farmer directory
├── templates/          # All HTML templates
│   ├── base.html       # Base layout with navbar
│   ├── register.html   # Registration page
│   ├── login.html      # Login page
│   ├── shop.html       # Product listing
│   ├── cart.html       # Shopping cart
│   ├── farmer_dashboard.html
│   ├── pending_orders.html
│   ├── order_history.html
│   └── farmer_contact.html  # Farmer directory
├── farmora/            # Project settings and URLs
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── Procfile            # Railway deployment

⚙️ Local Setup
1. Clone the repo
bashgit clone https://github.com/1tharun/FarmOra.git
cd FarmOra
2. Create and activate virtual environment
bashpython -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
3. Install dependencies
bashpip install -r requirements.txt
4. Run migrations
bashpython manage.py migrate
5. Start the server
bashpython manage.py runserver
Visit: http://127.0.0.1:8000

📧 Email Configuration
Emails are sent via Gmail SMTP. Update these in farmora/settings.py or set as environment variables:
pythonEMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Gmail App Password, not your real password
To generate a Gmail App Password:

Go to Google Account → Security
Enable 2-Step Verification
Search "App Passwords" → Generate one for "Mail"


🌐 Deployment (Railway)
1. Push to GitHub
bashgit add .
git commit -m "deploy"
git push
2. On Railway

New Project → Deploy from GitHub → Select FarmOra
Add Plugin → PostgreSQL
Add environment variables:

EMAIL_HOST_USER      = your-email@gmail.com
EMAIL_HOST_PASSWORD  = your-app-password
SECRET_KEY           = your-secret-key

Settings → Domains → Generate Domain

3. Start command (Railway Settings)
python manage.py migrate && python manage.py collectstatic --noinput && gunicorn farmora.wsgi

👥 User Roles
Farmer

Register with role = Farmer
Add/edit/delete products
View and manage pending orders
Accept or reject customer orders

Customer

Register with role = Customer
Browse products in the shop
Add to cart and place orders
View order history
Browse Farmer Directory


🗄️ Database Models
Account
FieldTypeDescriptionnameCharFieldFull nameemailEmailFieldUnique emailpasswordCharFieldPlain text (hash in production)roleCharFielduser or farmermobile_numberCharFieldPhone numberaddressTextFieldDelivery / farm addresscreated_atDateTimeFieldAccount creation time
Product
FieldTypeDescriptionnameCharFieldProduct nametelugu_nameCharFieldTelugu namepriceDecimalFieldPrice per unitimageURLFieldImage URLfarmer_idIntegerFieldLinked farmer
Order
FieldTypeDescriptionuser_idIntegerFieldCustomerfarmer_idIntegerFieldFarmerproductForeignKeyProduct orderedquantityIntegerFieldNumber of unitstotalDecimalFieldTotal pricestatusCharFieldpending / accepted / rejectedcreated_atDateTimeFieldOrder time

🔐 Security Notes

⚠️ This project is built for learning/demo purposes.

For production use:

Hash passwords using Django's built-in make_password
Set DEBUG = False
Use environment variables for all secrets
Enable HTTPS
Set up email verification


📞 Contact & Support
Built by Tharun · Hyderabad, India
GitHub: @1tharun

Farmora — Where the harvest meets the home. 🌿
