from django.contrib import admin
from django.urls import path, include
from accounts import views as acc_views
from products import views as prod_views
from dashboard import views as dash_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", acc_views.register),
    path("login/", acc_views.login_view),
    path("logout/", acc_views.logout_view),
    path("shop/", prod_views.shop),
    path("add/<int:id>/", prod_views.add_to_cart),
    path("minus/<int:id>/", prod_views.decrease_cart),
    path("cart/", prod_views.cart_view),
    path("place-order/", prod_views.place_order),
    path("orders/", prod_views.order_history),
    path("farmer-dashboard/", dash_views.farmer_dashboard),
    path("add-product/", dash_views.add_product),
    path("edit-product/<int:id>/", dash_views.edit_product),
    path("delete-product/<int:id>/", dash_views.delete_product),
    path("pending-orders/", dash_views.pending_orders),
    path("farmer-directory/", dash_views.farmer_contact_directory),
    path('remove/<int:id>/', prod_views.remove_from_cart),
    path("", include("orders.urls")),
]
