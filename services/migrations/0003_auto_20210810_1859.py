# Generated by Django 3.2.6 on 2021-08-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20210810_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_details',
            name='buy',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='card_details',
            name='sell',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
