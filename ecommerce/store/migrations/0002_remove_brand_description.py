# Generated by Django 5.1.1 on 2024-09-13 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='description',
        ),
    ]
