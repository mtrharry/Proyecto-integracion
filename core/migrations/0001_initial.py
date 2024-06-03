# Generated by Django 5.0.6 on 2024-06-03 14:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de Producto')),
                ('precio', models.IntegerField(verbose_name='Precio de Producto')),
            ],
        ),
        migrations.CreateModel(
            name='tipoProducto',
            fields=[
                ('idTipoProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de Tipo de Producto')),
                ('nombreTipoProducto', models.CharField(max_length=50, verbose_name='Nombre de Tipo de Producto')),
                ('descripcionTipoProducto', models.CharField(max_length=50, verbose_name='Descripcion de Tipo de Producto')),
            ],
        ),
        migrations.CreateModel(
            name='stockProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(null=True, verbose_name='Stock de Producto')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto', verbose_name='Id de Producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='cantidadstock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.stockproducto', verbose_name='Cantidad en Stock'),
        ),
        migrations.AddField(
            model_name='producto',
            name='idTipoProducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.tipoproducto', verbose_name='Id de Tipo de Producto'),
        ),
    ]
