# Generated by Django 5.0.6 on 2024-05-13 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_producto_idtipoproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='nombreProducto',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='tipoProducto',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
