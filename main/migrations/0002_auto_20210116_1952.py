# Generated by Django 3.0.5 on 2021-01-16 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.FileField(default=None, upload_to=None),
            preserve_default=False,
        ),
    ]
