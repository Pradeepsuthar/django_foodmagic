# Generated by Django 3.0.3 on 2020-02-22 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0004_auto_20200222_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='restaurant_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foodapp.Restaurant'),
        ),
    ]
