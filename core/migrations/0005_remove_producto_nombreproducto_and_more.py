# Generated by Django 5.0.6 on 2024-05-13 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tipoproducto_descripciontipoproducto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='nombreProducto',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precioProducto',
        ),
    ]
