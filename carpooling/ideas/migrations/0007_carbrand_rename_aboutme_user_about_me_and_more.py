# Generated by Django 4.1.4 on 2022-12-26 12:28

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0006_user_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='aboutme',
            new_name='about_me',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='passwd',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='driver',
        ),
        migrations.AddField(
            model_name='ride',
            name='baby_seat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ride',
            name='driver_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ride',
            name='trunk',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ride',
            name='allow_pets',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ride',
            name='arrival_date',
            field=models.DateTimeField(default='YYYY-MM-DD HH:MM'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='leave_date',
            field=models.DateTimeField(default='YYYY-MM-DD HH:MM'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default='YYYY-MM-DD'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+48XXXXXXXXX', max_length=128, region=None, unique=True),
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.carbrand')),
            ],
        ),
    ]
