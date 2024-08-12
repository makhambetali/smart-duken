# Generated by Django 5.0.7 on 2024-07-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sManager', '0013_remove_debt_customer_rename_seller_debt_creator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='debt',
            name='content',
            field=models.CharField(max_length=10, verbose_name='Операция'),
        ),
        migrations.AlterField(
            model_name='debt',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Доп. информация'),
        ),
    ]
