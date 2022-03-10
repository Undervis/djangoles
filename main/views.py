from django.shortcuts import render, get_object_or_404
from .models import Item


def home(request):
    items = Item.objects.all()[1:5]
    print(items.query)
    return render(request, 'home.html', {'items': items})
