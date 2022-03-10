from django.db import models


class Item(models.Model):
    name = models.CharField('Название', max_length=32)
    description = models.TextField('Описание')
    price = models.FloatField('Цена')
    img = models.ImageField('Фото', upload_to='static/images')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Название', max_length=32)

    def __str__(self):
        return self.name