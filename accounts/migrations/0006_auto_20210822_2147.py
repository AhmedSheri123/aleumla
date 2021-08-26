# Generated by Django 3.2.6 on 2021-08-22 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_alter_userprofile_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirm_account',
            name='is_finshed',
        ),
        migrations.AddField(
            model_name='confirm_account',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default="2002-2-2"),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Reset_Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
