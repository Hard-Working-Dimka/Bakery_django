from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    telegram_id = models.BigIntegerField(unique=True, blank=True, null=True)
    telegram_username = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username


class Cake(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class Modifications(models.Model):
    modification = models.TextField()

    def __str__(self):
        return self.modification


class VariablesOfModification(models.Model):
    modification = models.ForeignKey(Modifications, on_delete=models.CASCADE)
    tier = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.modification} --- {self.tier}'


class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    address = models.TextField()
    status = models.BooleanField(default=False)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, blank=True, null=True)
    cake_builder = models.ManyToManyField(VariablesOfModification, blank=True, null=True)
    delivery_date = models.DateField()
    phone_number = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} --- {self.cake}"
