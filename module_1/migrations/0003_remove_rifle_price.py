# Generated by Django 4.0.5 on 2023-03-28 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_1', '0002_rifle_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rifle',
            name='price',
        ),
    ]
