# Generated by Django 4.0.6 on 2022-07-20 20:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_api', '0002_alter_video_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='upload',
            field=models.FileField(upload_to='uploads/videos/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['mp4', 'mkv'])]),
        ),
    ]
