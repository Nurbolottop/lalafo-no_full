# Generated by Django 4.1.2 on 2022-10-27 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название продукта')),
                ('description', models.TextField(verbose_name='Описание продукта')),
                ('image', models.ImageField(upload_to='product_image/', verbose_name='Фотография продукта')),
                ('price', models.PositiveIntegerField(verbose_name='Цена продукта')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
