from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    telegram_id = models.BigIntegerField(unique=True, blank=True, null=True)
    telegram_username = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.telegram_username}"


class Cake(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='cake_photos')

    def __str__(self):
        return self.name


class Modifications(models.Model):
    modification = models.CharField(max_length=50)
    necessary = models.BooleanField()
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, related_name='modifications')

    def __str__(self):
        return self.modification


class VariablesOfModification(models.Model):
    modification = models.ForeignKey(Modifications, on_delete=models.CASCADE, related_name='variables_of_modification')
    tier = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.modification.cake} - {self.modification} ({self.tier})'


class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    address = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, related_name='orders')
    variables_of_modifications = models.ManyToManyField(VariablesOfModification, blank=True, null=True,
                                                        related_name='orders')
    delivery = models.DateTimeField()
    phone_number = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.customer}'
