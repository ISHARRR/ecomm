# Generated by Django 2.1.7 on 2019-03-24 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cart_subtotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='updated',
        ),
    ]
