# Generated by Django 4.2.1 on 2023-06-17 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameMate7', '0002_remove_producto_categoria_remove_producto_proveedor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]