# Generated by Django 2.2.4 on 2019-08-31 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_auto_20190830_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_category',
            name='offer',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='product_category',
            name='subCategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Product_Category'),
        ),
        migrations.AlterField(
            model_name='product_category',
            name='name',
            field=models.CharField(choices=[('MB', 'MOBILE'), ('HF', 'HEADPHONE'), ('WA', 'WATCHES')], max_length=50),
        ),
    ]
