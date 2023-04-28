from rest_framework import serializers
from .models import Order , OrderDetail



class OrderListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = '__all__'