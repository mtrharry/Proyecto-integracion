# Generated by Django 5.0.6 on 2024-05-13 02:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_producto_idtipoproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='idTipoProducto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.tipoproducto', verbose_name='Id de Tipo de Producto'),
            preserve_default=False,
        ),
    ]