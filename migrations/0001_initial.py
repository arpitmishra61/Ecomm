# Generated by Django 2.2.4 on 2019-08-03 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('MB', 'MB'), ('HF', 'HF'), ('WA', 'WA')], default='MOBILES', max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('off_price', models.IntegerField()),
                ('offer', models.BooleanField()),
                ('most_popular', models.BooleanField()),
                ('fantastic', models.BooleanField()),
                ('mainImage', models.ImageField(upload_to='products/{name}/')),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('stars', models.IntegerField()),
                ('description', models.TextField()),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(height_field=200, upload_to='products/', width_field=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.BigIntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('alternative_mobile', models.BigIntegerField(blank=True, null=True)),
                ('userImage', models.ImageField(upload_to='photos/user/')),
                ('cart_products', models.ManyToManyField(to='backend.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Product_Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='subImages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Product_Image'),
        ),
    ]
