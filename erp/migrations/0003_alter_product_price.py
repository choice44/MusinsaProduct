# Generated by Django 4.2 on 2023-04-06 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]
