# Generated by Django 4.0 on 2022-02-11 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0026_buyer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='name',
            field=models.CharField(default='None', max_length=30),
        ),
    ]