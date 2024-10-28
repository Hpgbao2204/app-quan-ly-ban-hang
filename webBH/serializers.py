from rest_framework import serializers
from .models import Product, Profile
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'code', 'brand', 'category']
        extra_kwargs = {
            'code': {'read_only': True},  # Đặt code là read-only
        }


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = Profile
        fields = ['username', 'password', 'address', 'phone', 'email']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(
            username=user_data['username'],
            password=validated_data['password'],
            email=user_data['email']
        )
        user_info = Profile.objects.create(
            user=user,
            address=validated_data['address'],
            phone=validated_data['phone']
        )
        return user_info
