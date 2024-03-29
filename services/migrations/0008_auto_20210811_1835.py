# Generated by Django 3.2.6 on 2021-08-11 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20210811_1719'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Card_Details',
            new_name='Dollars',
        ),
        migrations.CreateModel(
            name='Golds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('buy', models.DecimalField(decimal_places=2, max_digits=9)),
                ('sell', models.DecimalField(decimal_places=2, max_digits=9)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.city')),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.materials')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.type')),
            ],
        ),
        migrations.CreateModel(
            name='Euros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('buy', models.DecimalField(decimal_places=2, max_digits=9)),
                ('sell', models.DecimalField(decimal_places=2, max_digits=9)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.city')),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.materials')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.type')),
            ],
        ),
    ]
