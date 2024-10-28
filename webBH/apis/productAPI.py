from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from drf_spectacular.utils import extend_schema
from webBH.models import Product
from webBH.serializers import ProductSerializer
import strgen


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
    lookup_field = 'code'

    @extend_schema(
        summary="Mô tả sản phẩm",
        description="Thông tin chi tiết sản phẩm theo ID",
        responses={200: ProductSerializer},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# @api_view(['POST'])
# @permission_classes([AllowAny])
# def product_create_view(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         code = strgen.StringGenerator(r"[\d]{8}").render()
#         serializer.save(code=code)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Viết api thêm sản phẩm sử dụng @api_view và @permission_classes
@api_view(['POST'])
@permission_classes([AllowAny])
@extend_schema(
    summary="Tạo sản phẩm",
    description="Tạo mới một sản phẩm",
    responses={200: ProductSerializer},
)
def product_create_view(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        code = strgen.StringGenerator(r"[\d]{8}").render()
        serializer.save(code=code)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'code'

    @extend_schema(
        summary="Sửa sản phẩm",
        description="Sửa thông tin sản phẩm theo ID",
        responses={200: ProductSerializer},
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def perform_create(self, serializer):
        code = strgen.StringGenerator(r"[\d]{8}").render()
        serializer.save(code=code)


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'code'

    @extend_schema(
        summary="Xóa sản phẩm",
        description="Xóa sản phẩm theo ID",
        responses={200: ProductSerializer},
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

