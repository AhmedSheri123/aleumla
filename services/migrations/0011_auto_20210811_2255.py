# Generated by Django 3.2.6 on 2021-08-11 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_auto_20210811_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='materials',
            name='informtions',
            field=models.TextField(default='|link id| |for dollars = 1 and set name (دولار)| |for Euros = 2 and set name (يورو)| |for golds = 3 and set name (ذهب)|'),
        ),
        migrations.AddField(
            model_name='materials',
            name='link',
            field=models.IntegerField(default=0),
        ),
    ]
