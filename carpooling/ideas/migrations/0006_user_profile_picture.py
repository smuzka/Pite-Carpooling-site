# Generated by Django 4.1.4 on 2022-12-17 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0005_user_aboutme_user_birth_date_user_join_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='pfps'),
        ),
    ]
