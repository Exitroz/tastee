from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from .models import Food, OrderItem, Order, Ingredient


# Create your views here.

def home(request):
    foods = Food.objects.all()
    
    context = {'foods': foods}
    return render(request, 'base/index.html', context)

def foodItem(request, pk):
    food = Food.objects.get(id=pk)
    
    context = {'food': food}
    return render(request, 'base/product.html', context)


def add_to_cart(request, pk):
    item = get_object_or_404(Food, id=pk)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    # Check if the user has a pending item in cart 
    
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # Check if order item is in order 
        if order.items.filter(item__name=item.name).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        order = Order.objects.create(user=request.user)
        order.item.add(order_item)
    return redirect('food-item', pk=item.id)


        

