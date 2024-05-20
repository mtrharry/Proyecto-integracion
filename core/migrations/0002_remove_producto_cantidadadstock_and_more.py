# Generated by Django 5.0.6 on 2024-05-20 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cantidadadstock',
        ),
        migrations.AddField(
            model_name='producto',
            name='cantidadstock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.stockproducto', verbose_name='Cantidad en Stock'),
        ),
        migrations.AlterField(
            model_name='stockproducto',
            name='cantidad',
            field=models.IntegerField(null=True, verbose_name='Stock de Producto'),
        ),
        migrations.AlterField(
            model_name='stockproducto',
            name='idProducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto', verbose_name='Id de Producto'),
        ),
    ]
