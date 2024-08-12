# Generated by Django 5.0.7 on 2024-07-28 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sManager', '0022_money_datetime_alter_money_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='second_name',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='tel_number_salesman_reserve',
        ),
        migrations.AddField(
            model_name='supplier',
            name='delivery',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Доставка'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='extra_info',
            field=models.TextField(blank=True, null=True, verbose_name='Доп. информация'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='tel_number_delivery',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер Телефона (Доставка)'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='tel_number_salesman',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер Телефона (торг. представитель)'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='tel_number_supervisor',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер Телефона (супервайзер)'),
        ),
    ]