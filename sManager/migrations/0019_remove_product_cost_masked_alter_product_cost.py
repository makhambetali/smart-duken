# Generated by Django 5.0.7 on 2024-07-26 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sManager', '0018_product_cash_amount_product_transfer_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cost_masked',
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.CharField(max_length=9),
        ),
    ]