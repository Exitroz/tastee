from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Food, OrderItem, Order, Ingredient


# Create your views here.

def home(request):
    foods = Food.objects.all()
    
    context = {'foods': foods}
    return render(request, 'base/index.html', context)

def foodItem(request, pk):
    food_item = Food.objects.get(id=pk)
    
    context = {'food_item': food_item}
    return render(request, 'base/product.html', context)


