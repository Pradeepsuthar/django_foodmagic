# Generated by Django 3.0.3 on 2020-02-22 10:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_img', models.ImageField(null=True, upload_to='images\\restaurants-img\\')),
                ('restaurant_name', models.CharField(max_length=400)),
                ('restaurant_address', models.CharField(default='Restaurant Current Address', max_length=100)),
                ('restaurant_owner', models.CharField(max_length=200)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('restaurant_owner_phone_no', models.CharField(default='0000000000', max_length=10, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)]),
        ),
    ]