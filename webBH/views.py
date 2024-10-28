from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .models import UserInfo
from django.utils.timezone import now
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from .serializers import UserInfoSerializer
from rest_framework import (status,
                            generics)


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Ghi lại user agent
        response = super().authenticate(request)

        return response


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # Thực hiện yêu cầu đăng nhập
        response = super().post(request, *args, **kwargs)

        # Lấy thông tin từ response data của serializer (nếu đăng nhập thành công)
        if response.status_code == status.HTTP_200_OK:
            user = self.get_user_from_credentials(request.data)

            if user:
                user_agent = request.META.get('HTTP_USER_AGENT', '')
                # Lưu hoặc cập nhật UserAgent
                UserInfo.objects.update_or_create(user=user, defaults={'user_agent': user_agent})

        return response

    def get_user_from_credentials(self, data):
        """
        Phương thức để lấy đối tượng người dùng từ thông tin đăng nhập
        """
        from django.contrib.auth import authenticate

        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                return user
        return None


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        # Lưu thông tin user agent sau khi đăng nhập
        request = self.context['request']
        user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')

        # Lưu vào database hoặc log lại
        user.last_login = now()
        user.user_agent = user_agent  # Ví dụ nếu bạn có trường user_agent trong model User
        user.save()

        return data


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()


class CustomLoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


@api_view(['GET'])
def user_info(request):
    return Response({
        'username': request.user.username,
    })


@api_view(['GET'])
def protected_view(request):
    # Chỉ người dùng đã xác thực bằng JWT mới được truy cập
    request.user  # Đây là thông tin của người dùng hiện tại
    return Response({'message': 'You are authenticated!'})

