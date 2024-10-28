import strgen

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product


@receiver(post_save, sender=Product)
def handle_todo_created(sender, instance: Product, created, **kwargs):
    # Tạo mã công việc gồm 8 chữ số
    if not instance.code:
        code = strgen.StringGenerator(r"[\d]{8}").render()
        instance.code = code
        Product.objects.filter(id=instance.id).update(code=code)