# Generated by Django 2.2.4 on 2019-08-04 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20190804_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='firstImage',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='mainImage',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='secondImage',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thirdImage',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
