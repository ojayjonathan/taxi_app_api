# Generated by Django 3.2.6 on 2021-08-05 16:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20210805_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='time',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 8, 5, 16, 54, 46, 270371, tzinfo=utc)),
        ),
    ]
