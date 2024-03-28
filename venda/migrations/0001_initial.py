# Generated by Django 5.0.3 on 2024-03-28 17:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tipo_produto', models.CharField(choices=[('ALCOOLICA', 'Alcoólica'), ('NAO ALCOOLICA', 'Não Alcoólica')], max_length=15)),
                ('qtd', models.IntegerField(default=0)),
                ('preco_vendas', models.FloatField(default=0)),
                ('total_gasto', models.FloatField(default=0)),
                ('data_criaco', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
