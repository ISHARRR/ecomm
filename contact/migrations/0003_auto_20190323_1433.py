# Generated by Django 2.1.7 on 2019-03-23 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20190323_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmodel',
            old_name='content',
            new_name='message',
        ),
    ]
