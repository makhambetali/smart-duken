# Generated by Django 5.0.7 on 2024-07-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sManager', '0019_remove_product_cost_masked_alter_product_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.PositiveIntegerField(max_length=9),
        ),
    ]