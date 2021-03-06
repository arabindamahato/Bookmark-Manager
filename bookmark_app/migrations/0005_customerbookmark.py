# Generated by Django 3.0.6 on 2020-05-16 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark_app', '0004_remove_bookmark_bookmark_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmark_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmark_app.Bookmark')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmark_app.Customer')),
            ],
        ),
    ]
