# Generated by Django 4.1.3 on 2022-11-12 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_product_like', to='products.product', verbose_name='Продукт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_like_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Понравшиеся посты',
                'verbose_name_plural': 'Понравшиеся посты',
            },
        ),
    ]
