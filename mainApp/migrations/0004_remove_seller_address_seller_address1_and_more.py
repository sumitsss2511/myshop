# Generated by Django 4.0 on 2022-02-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='address',
        ),
        migrations.AddField(
            model_name='seller',
            name='address1',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='address2',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
