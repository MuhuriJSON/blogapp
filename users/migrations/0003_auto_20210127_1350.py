# Generated by Django 2.2 on 2021-01-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210125_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default2.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
