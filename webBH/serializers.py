from rest_framework import serializers
from .models import Product, UserInfo
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'code']


class UserInfoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = UserInfo
        fields = ['username', 'password', 'address', 'phone', 'email']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(
            username=user_data['username'],
            password=validated_data['password'],
            email=user_data['email']
        )
        user_info = UserInfo.objects.create(
            user=user,
            address=validated_data['address'],
            phone=validated_data['phone']
        )
        return user_info
