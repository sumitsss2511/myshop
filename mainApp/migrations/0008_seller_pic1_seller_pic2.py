# Generated by Django 4.0 on 2022-02-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='pic1',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='seller',
            name='pic2',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
    ]