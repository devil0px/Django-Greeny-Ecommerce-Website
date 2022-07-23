# Generated by Django 3.2 on 2022-07-23 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserAddress', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userphonenumber',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserPhone', to=settings.AUTH_USER_MODEL),
        ),
    ]
