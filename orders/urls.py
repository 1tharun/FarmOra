from django.urls import path
from . import views

urlpatterns = [
    path('accept-order/<int:id>/', views.accept_order),
    path('reject-order/<int:id>/', views.reject_order),
    path('out-for-delivery/<int:id>/', views.mark_out_for_delivery),
    path('mark-delivered/<int:id>/', views.mark_delivered),
]
