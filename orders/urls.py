from django.urls import path
from . import views

urlpatterns = [
    path('accept-order/<int:id>/', views.accept_order, name='accept_order'),
    path('reject-order/<int:id>/', views.reject_order, name='reject_order'),
]
