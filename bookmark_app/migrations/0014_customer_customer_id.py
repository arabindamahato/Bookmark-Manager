# Generated by Django 3.0.6 on 2020-05-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark_app', '0013_auto_20200517_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(blank=True, default='C001', max_length=10),
        ),
    ]
