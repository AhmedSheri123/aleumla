# Generated by Django 3.2.6 on 2021-08-17 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0021_auto_20210816_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Confirm_Account',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
