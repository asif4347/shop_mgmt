# Generated by Django 2.1.7 on 2019-02-17 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('In Progress', 'In progress'), ('Completed', 'completed')], default='In Progress', max_length=25)),
                ('total_amount', models.IntegerField()),
                ('amount_paid', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Salesman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='salesman',
            name='shops',
            field=models.ManyToManyField(null=True, to='app1.Shop'),
        ),
        migrations.AddField(
            model_name='orders',
            name='products',
            field=models.ManyToManyField(to='app1.Product'),
        ),
        migrations.AddField(
            model_name='orders',
            name='salesman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Salesman'),
        ),
        migrations.AddField(
            model_name='amount',
            name='delivery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Orders'),
        ),
    ]