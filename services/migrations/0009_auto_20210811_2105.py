# Generated by Django 3.2.6 on 2021-08-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20210811_1835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dollars',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AlterField(
            model_name='dollars',
            name='publish_date',
            field=models.DateTimeField(),
        ),
    ]
