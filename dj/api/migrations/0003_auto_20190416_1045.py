# Generated by Django 2.1.4 on 2019-04-16 02:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190411_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='session',
            name='session_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
