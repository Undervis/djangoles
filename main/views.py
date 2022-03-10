from django.shortcuts import render, get_object_or_404
from .models import Item


def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
