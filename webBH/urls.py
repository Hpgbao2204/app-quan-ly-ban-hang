from django.urls import path

from webBH.apis.productAPI import (ProductListView,
                                   ProductDetailView,
                                   product_create_view,
                                   ProductUpdateView,
                                   ProductDeleteView)

from rest_framework_simplejwt.views import TokenRefreshView

from .views import (CustomTokenObtainPairView, CreateUserView, CustomLoginView)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<str:code>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', product_create_view, name='product-create'),
    path('products/update/<str:code>/', ProductUpdateView.as_view(), name='product-update'),
    path('products/delete/<str:code>/', ProductDeleteView.as_view(), name='product-delete'),


    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/register/', CreateUserView.as_view(), name='token_register'),
    path('token/login/', CustomLoginView.as_view(), name='token_login'),
]
