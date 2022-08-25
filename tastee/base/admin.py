from django.contrib import admin
from .models import User, Food, OrderItem, Order
# Register your models here.


admin.site.register(User)
admin.site.register(Food)
admin.site.register(OrderItem)
admin.site.register(Order)