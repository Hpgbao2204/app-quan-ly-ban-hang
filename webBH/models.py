from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    """
    Brand model
    """
    brand_name = models.CharField(max_length=200, help_text="Nhập tên hãng")

    def __str__(self):
        return self.brand_name


class Categories(models.Model):
    """
    Categories model
    """
    category_name = models.CharField(max_length=200, help_text="Nhập tên loại sản phẩm")

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """
    Product model
    """
    name = models.CharField(max_length=200, help_text="Nhập tên sản phẩm")
    price = models.FloatField(help_text="Nhập giá sản phẩm")
    description = models.TextField(help_text="Nhập mô tả sản phẩm")
    code = models.CharField(max_length=8, blank=True, help_text="Mã sản phẩm", null=True, unique=True)
    brand = models.ForeignKey(Brand, help_text="Chọn hãng sản xuất", null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Categories, help_text="Chọn loại sản phẩm", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    """
    UserInfo model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, help_text="Nhập địa chỉ")
    phone = models.CharField(max_length=20, help_text="Nhập số điện thoại")

    def __str__(self):
        return self.user.username

