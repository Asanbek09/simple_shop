# Generated by Django 4.2.13 on 2024-05-21 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='updates',
            new_name='updated',
        ),
    ]
