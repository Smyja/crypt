# Generated by Django 3.0.6 on 2020-08-01 02:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200105_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='contentt',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
