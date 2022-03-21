from django.shortcuts import render, get_object_or_404
from .models import *


def home(request):
    if request.GET.get('category'):
        category = Category.objects.get(pk=request.GET['category'])
        items = Item.objects.filter(category=category)
    else:
        items = Item.objects.all()

    categories = Category.objects.all()
    return render(request, 'home.html', {'items': items, 'categories': categories})
