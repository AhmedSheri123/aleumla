# Generated by Django 3.2.6 on 2021-08-11 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_materials_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materials',
            name='type',
        ),
    ]
