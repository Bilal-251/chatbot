# Generated by Django 5.0 on 2023-12-05 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arsi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_rating',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=3, verbose_name='product rating'),
        ),
    ]
