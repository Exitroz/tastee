from django.contrib import admin
from .models import User, Food, OrderItem, Order, Ingredient
# Register your models here.


admin.site.register(User)
admin.site.register(Food)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Ingredient)