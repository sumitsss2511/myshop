# Generated by Django 4.0 on 2022-02-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0029_alter_buyer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='phone',
            field=models.CharField(default=0, max_length=15),
        ),
    ]