# Generated by Django 3.2.6 on 2021-08-22 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210822_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reset_password',
            name='key',
            field=models.CharField(max_length=400, unique=True),
        ),
    ]