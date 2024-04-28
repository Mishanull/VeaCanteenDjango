from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=25)

    def price(self):
        return 0

    def __str__(self):
        return self.name


class Drink(Product):
    COFFEE = 'Coffee'
    JUICE = 'Juice'
    TEA = 'Tea'
    DRINK_TYPE_CHOICES = [
        (COFFEE, 'Coffee'),
        (JUICE, 'Juice'),
        (TEA, 'Tea'),
    ]

    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    DRINK_SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]

    type = models.CharField(max_length=255, choices=DRINK_TYPE_CHOICES)
    size = models.CharField(max_length=255, choices=DRINK_SIZE_CHOICES)

    def get_base_price(self):
        # Here you would implement logic to return base price for a drink type
        # For example:
        if self.type == self.COFFEE:
            return 2.0
        elif self.type == self.JUICE:
            return 2.5
        elif self.type == self.TEA:
            return 1.5
        else:
            return 0  # Default case

    def get_size_addition(self):
        # Returns additional price based on the size of the drink
        if self.size == self.SMALL:
            return 0
        elif self.size == self.MEDIUM:
            return 0.5
        elif self.size == self.LARGE:
            return 1.0
        else:
            return 0  # Default case

    def price(self):
        return self.get_base_price() + self.get_size_addition()


class Food(Product):
    BREAD = 'Bread'
    DESSERT = 'Dessert'
    SALAD = 'Salad'
    WARM_FOOD = 'WarmFood'
    FOOD_TYPE_CHOICES = [
        (BREAD, 'Bread'),
        (DESSERT, 'Dessert'),
        (SALAD, 'Salad'),
        (WARM_FOOD, 'Warm Food'),
    ]

    type = models.CharField(max_length=255, choices=FOOD_TYPE_CHOICES)

    def get_base_price(self):
        if self.type == self.BREAD:
            return 1.0
        elif self.type == self.DESSERT:
            return 3.0
        elif self.type == self.SALAD:
            return 5.0
        elif self.type == self.WARM_FOOD:
            return 8.0
        else:
            return 0  # Default case

    def price(self):
        return self.get_base_price()


class Order(models.Model):
    drinks = models.ManyToManyField(Drink)
    food = models.ManyToManyField(Food)
    name = models.CharField(max_length=25)

    def total_price(self):
        return sum([drink.price() for drink in self.drinks.all()]) + sum([food.price() for food in self.food.all()])
