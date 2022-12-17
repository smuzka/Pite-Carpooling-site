# Generated by Django 4.1.4 on 2022-12-17 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0004_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='aboutme',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='join_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]