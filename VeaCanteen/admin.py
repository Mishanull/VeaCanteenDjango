from django.contrib import admin

from VeaCanteen.models import Food, Drink, Order


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'size', 'price']


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_price']
