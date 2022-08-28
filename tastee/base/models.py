from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings

# Create your models here.
CATEGORY_CHOICES = (
    ('M', 'Main dish'),
    ('D', 'Desert'),
    ('DR', 'Drinks')
)

class User(AbstractUser):
    full_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(null=True, default="avatar.svg")
    
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    
 
class Ingredient(models.Model):
    name = models.CharField(max_length=100) 
    
    
    def __str__(self):
        return self.name
      
class Food(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    description = models.TextField(max_length=255)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    image = models.ImageField(default='3.jpg', upload_to='food-images', null=True, blank=True)
    price = models.FloatField()
    available = models.BooleanField(default=True)
    
    class Meta:
        ordering = []
        
    
    def __str__(self):
        return self.name


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Food, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.name}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    
    
