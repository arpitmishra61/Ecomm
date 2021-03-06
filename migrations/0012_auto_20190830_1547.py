# Generated by Django 2.2.4 on 2019-08-30 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_showcase_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product_review',
            options={'ordering': ('date_published',)},
        ),
        migrations.RemoveField(
            model_name='product',
            name='reviews',
        ),
        migrations.RemoveField(
            model_name='product_review',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='reviews',
        ),
        migrations.AddField(
            model_name='product_review',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Product'),
        ),
    ]
