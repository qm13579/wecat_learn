# Generated by Django 2.1.4 on 2019-04-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uasername', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('age', models.CharField(max_length=12)),
            ],
        ),
    ]
