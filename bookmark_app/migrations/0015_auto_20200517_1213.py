# Generated by Django 3.0.6 on 2020-05-17 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark_app', '0014_customer_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(blank=True, default='C001', max_length=10, unique=True),
        ),
    ]
