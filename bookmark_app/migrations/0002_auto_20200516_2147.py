# Generated by Django 3.0.6 on 2020-05-16 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
