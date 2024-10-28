from rest_framework import generics
from drf_spectacular.utils import extend_schema
from webBH.models import Product
from webBH.serializers import ProductSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(
        summary="Liệt kê sản phẩm",
        description="Trả về danh sách tất cả sản phẩm",
        responses={200: ProductSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(
        summary="Mô tả sản phẩm",
        description="Thông tin chi tiết sản phẩm theo ID",
        responses={200: ProductSerializer},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(
        summary="Tạo sản phẩm",
        description="Tạo mới một sản phẩm",
        responses={200: ProductSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(
        summary="Sửa sản phẩm",
        description="Sửa thông tin sản phẩm theo ID",
        responses={200: ProductSerializer},
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(
        summary="Xóa sản phẩm",
        description="Xóa sản phẩm theo ID",
        responses={200: ProductSerializer},
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

