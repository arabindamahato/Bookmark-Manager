# Generated by Django 3.0.6 on 2020-05-16 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark_app', '0002_auto_20200516_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=255)),
                ('url', models.URLField()),
                ('source_name', models.CharField(blank=True, default='', max_length=255)),
                ('bookmark_date', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='latitude',
            field=models.FloatField(blank=True, help_text='FloatField', null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='longitude',
            field=models.FloatField(blank=True, help_text='FloatField', null=True),
        ),
    ]
