# Generated by Django 2.1.7 on 2019-03-03 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_remove_orderproducts_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproducts',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.Product'),
            preserve_default=False,
        ),
    ]
