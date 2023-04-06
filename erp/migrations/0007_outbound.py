# Generated by Django 4.2 on 2023-04-06 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_product_stock_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outbound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=3)),
                ('inbound_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=0, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.product')),
            ],
        ),
    ]
