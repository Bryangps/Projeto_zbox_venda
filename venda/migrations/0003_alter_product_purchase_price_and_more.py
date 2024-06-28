# Generated by Django 5.0.4 on 2024-06-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0002_remove_stock_maximum_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]