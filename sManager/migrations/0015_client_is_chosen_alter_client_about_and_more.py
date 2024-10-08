# Generated by Django 5.0.7 on 2024-07-25 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sManager', '0014_client_phone_number_alter_debt_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_chosen',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='about',
            field=models.TextField(blank=True, null=True, verbose_name='Доп. информация'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Имя Клиента'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер Телефона'),
        ),
    ]
