# Generated by Django 4.2 on 2024-01-21 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sManager', '0005_delete_productimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('supply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='sManager.product')),
            ],
        ),
    ]
