# Generated by Django 2.1.7 on 2019-02-18 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_orderproducts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='quantity_in_stock',
        ),
    ]
