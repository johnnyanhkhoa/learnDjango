# Generated by Django 4.0.5 on 2023-04-03 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_1', '0003_remove_rifle_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]