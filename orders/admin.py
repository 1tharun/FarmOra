from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user_id', 'farmer_id', 'quantity', 'total', 'status', 'created_at')
    list_filter = ('status',)
