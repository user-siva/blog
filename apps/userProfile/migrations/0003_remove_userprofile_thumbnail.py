# Generated by Django 3.2 on 2021-05-10 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0002_auto_20210510_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='thumbnail',
        ),
    ]
