# Generated by Django 4.0 on 2022-02-09 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0020_product_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.CASCADE, to='mainApp.seller'),
        ),
    ]
