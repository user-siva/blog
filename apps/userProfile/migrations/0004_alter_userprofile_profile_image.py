# Generated by Django 3.2 on 2021-05-10 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0003_remove_userprofile_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='default.jpg', upload_to='uploads/'),
        ),
    ]
