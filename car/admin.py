from django.contrib import admin
from car.models import Car, Category, Ingredient

# Register your models here.

admin.site.register(Car)
admin.site.register(Category)
admin.site.register(Ingredient)