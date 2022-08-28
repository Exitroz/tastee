from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('food-item/<str:pk>/', views.foodItem, name="food-item"),
    path('add-to-cart/<str:pk>/', views.add_to_cart, name="add-to-cart"),
    
]
