# Generated by Django 4.2 on 2024-03-02 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sManager', '0007_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='num',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Default_pfp.svg/510px-Default_pfp.svg.png?20220226140232', upload_to='users_images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
