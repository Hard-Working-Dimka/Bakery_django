from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
import requests
from django.conf import settings


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
    variables_of_modifications = models.TextField(blank=True, null=True)
    delivery = models.DateTimeField()
    phone_number = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.customer}'


class ShortenedURL(models.Model):
    long_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    click_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            try:
                unique_long_url = f"{self.long_url}#{uuid.uuid4().hex[:6]}"
                full_short_url = self.get_vk_short_url(unique_long_url)
                self.short_url = full_short_url.split('/')[-1]
            except Exception as e:
                self.short_url = uuid.uuid4().hex[:8]
        super().save(*args, **kwargs)

    @staticmethod
    def get_vk_short_url(long_url):
        access_token = settings.VK_ACCESS_TOKEN
        api_version = '5.131'

        url = f'https://api.vk.com/method/utils.getShortLink'
        params = {
            'url': long_url,
            'access_token': access_token,
            'v': api_version,
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'response' in data:
                return data['response']['short_url']
            else:
                raise ValueError(f"Ошибка при сокращении ссылки: {data.get('error', {}).get('error_msg', 'Неизвестная ошибка')}")
        else:
            raise ValueError(f"Ошибка при запросе к API ВКонтакте: {response.status_code}")

    def __str__(self):
        return f'{self.long_url} -> {self.short_url} (Clicks: {self.click_count})'
