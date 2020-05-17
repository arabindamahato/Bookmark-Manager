# Generated by Django 3.0.6 on 2020-05-16 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark_app', '0006_auto_20200517_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='customer_bookmark',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookmark', to='bookmark_app.CustomerBookmark'),
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_bookmark',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='bookmark_app.CustomerBookmark'),
        ),
        migrations.AlterField(
            model_name='customerbookmark',
            name='customer_bookmark_id',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]