# Generated by Django 2.2.1 on 2019-05-29 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='active',
            new_name='summary',
        ),
    ]
