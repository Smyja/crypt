# Generated by Django 2.2.9 on 2020-01-05 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headline',
            name='slug',
        ),
    ]