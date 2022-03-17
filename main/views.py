from django.shortcuts import render, get_object_or_404
from .models import *


def home(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'items': items, 'categories': categories})
