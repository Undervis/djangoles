from django.contrib import admin

from .models import *


class AdminItem(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category')
    list_filter = ('category', )
    search_fields = ('name__contains', )

# MHsYkA6R
admin.site.register(Item, AdminItem)
admin.site.register(Category)