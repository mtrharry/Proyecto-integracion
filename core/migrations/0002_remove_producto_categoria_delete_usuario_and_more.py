# Generated by Django 5.0.4 on 2024-05-05 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
