# Generated by Django 3.2.6 on 2021-08-13 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='object',
        ),
        migrations.AddField(
            model_name='details',
            name='materials',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='services.materials'),
            preserve_default=False,
        ),
    ]
