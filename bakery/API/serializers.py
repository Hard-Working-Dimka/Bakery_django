from rest_framework import serializers
from cakes.models import Cake, CustomUser, Modifications, VariablesOfModification, Order


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = '__all__'


class VariablesOfModificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariablesOfModification
        fields = ['id', 'tier', 'price']


class ModificationsSerializer(serializers.ModelSerializer):
    all = VariablesOfModificationSerializer(many=True, read_only=True)

    class Meta:
        model = Modifications
        fields = ['id', 'modification', 'necessary', 'all']


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(slug_field='telegram_id', queryset=CustomUser.objects.all())
    cake = serializers.SlugRelatedField(slug_field='name', queryset=Cake.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'address', 'status', 'delivery', 'phone_number', 'created', 'comment', 'customer', 'cake',
                  'variables_of_modifications']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'telegram_id', 'telegram_username']
