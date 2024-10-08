# Generated by Django 5.0.7 on 2024-07-26 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sManager', '0017_money'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cash_amount',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Наличка:'),
        ),
        migrations.AddField(
            model_name='product',
            name='transfer_amount',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Банковский счёт:'),
        ),
    ]
