from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.

def home(request):
    
    context = {}
    return render(request, 'base/index.html', context)