# Generated by Django 3.2.6 on 2021-08-13 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_auto_20210813_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='golds',
            name='score',
            field=models.IntegerField(default=21),
        ),
    ]
