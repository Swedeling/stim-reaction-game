# Generated by Django 4.0.4 on 2022-05-22 10:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_alter_game_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 22, 10, 57, 42, 429654, tzinfo=utc)),
        ),
    ]
