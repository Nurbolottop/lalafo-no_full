from django.db import models
from apps.users.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(
        User, on_delete = models.CASCADE,
        related_name = "product_user"
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название продукта"
    )
    description = models.TextField(
        verbose_name = "Описание продукта"
    )
    image = models.ImageField(
        upload_to = 'product_image/',
        verbose_name = "Фотография продукта"
    )
    price = models.PositiveIntegerField(
        verbose_name = "Цена продукта"
    )
    created = models.DateTimeField(
        auto_now_add = True
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_image",
        verbose_name="Продукт"
    )
    image = models.ImageField(
        upload_to="product_image/",
        verbose_name="фотография"
    )

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = "Дополнительная фотография"
        verbose_name_plural = "Дополнительные фотография"

class ProductLike(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="product_like_user",

    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_product_like",
        verbose_name="Продукт"
    )
    def __str__(self):
        return f"{self.user} {self.product}"

    class Meta:
        verbose_name = "Понравшиеся посты"
        verbose_name_plural = "Понравшиеся посты"