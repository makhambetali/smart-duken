# Generated by Django 5.0.7 on 2024-07-27 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sManager', '0020_alter_product_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Доп. информация'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.CharField(max_length=9),
        ),
    ]