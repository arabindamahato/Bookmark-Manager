# Generated by Django 3.0.6 on 2020-05-17 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark_app', '0015_auto_20200517_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='title_contains',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
