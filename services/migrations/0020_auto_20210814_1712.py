# Generated by Django 3.2.6 on 2021-08-14 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0019_details_score_for_gold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.city', verbose_name='المدينة'),
        ),
        migrations.AlterField(
            model_name='details',
            name='is_enable',
            field=models.BooleanField(default=True, verbose_name='تفعيل'),
        ),
        migrations.AlterField(
            model_name='details',
            name='materials',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.materials', verbose_name='المادة'),
        ),
        migrations.AlterField(
            model_name='details',
            name='score_for_gold',
            field=models.IntegerField(default=21, verbose_name='عيار الذهب'),
        ),
        migrations.AlterField(
            model_name='golds',
            name='buy',
            field=models.IntegerField(default=0, verbose_name='سعر الشراء'),
        ),
        migrations.AlterField(
            model_name='golds',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.city', verbose_name='المدينة'),
        ),
        migrations.AlterField(
            model_name='golds',
            name='materials',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.materials', verbose_name='المادة'),
        ),
        migrations.AlterField(
            model_name='golds',
            name='name',
            field=models.CharField(max_length=100, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='golds',
            name='publish_date',
            field=models.DateTimeField(verbose_name='تاريخ النشر'),
        ),
        migrations.AlterField(
            model_name='golds',
            name='score',
            field=models.IntegerField(default=21, verbose_name='عيار الذهب'),
        ),
        migrations.AlterField(
            model_name='golds',
            name='sell',
            field=models.IntegerField(default=0, verbose_name='سعر البيع'),
        ),
        migrations.AlterField(
            model_name='golds',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.type', verbose_name='النوع'),
        ),
        migrations.AlterField(
            model_name='show_in_index',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.city', verbose_name='المدينة'),
        ),
        migrations.AlterField(
            model_name='show_in_index',
            name='is_show',
            field=models.BooleanField(default=False, verbose_name='اظهار في الصفحة الرئيسية'),
        ),
        migrations.AlterField(
            model_name='show_in_index',
            name='materials',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.materials', verbose_name='المادة'),
        ),
        migrations.AlterField(
            model_name='show_in_index',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.type', verbose_name='النوع'),
        ),
        migrations.CreateModel(
            name='Turkish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='الاسم')),
                ('buy', models.IntegerField(default=0, verbose_name='سعر الشراء')),
                ('sell', models.IntegerField(default=0, verbose_name='سعر البيع')),
                ('publish_date', models.DateTimeField(verbose_name='تاريخ النشر')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.city', verbose_name='المدينة')),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.materials', verbose_name='المادة')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.type', verbose_name='النوع')),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
        migrations.CreateModel(
            name='Saudi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='الاسم')),
                ('buy', models.IntegerField(default=0, verbose_name='سعر الشراء')),
                ('sell', models.IntegerField(default=0, verbose_name='سعر البيع')),
                ('publish_date', models.DateTimeField(verbose_name='تاريخ النشر')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.city', verbose_name='المدينة')),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.materials', verbose_name='المادة')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.type', verbose_name='النوع')),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]
