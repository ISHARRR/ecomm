# Generated by Django 2.1.7 on 2019-03-12 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_productmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
