# Generated by Django 4.0.4 on 2022-05-24 07:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_alter_game_result_alter_game_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 24, 7, 48, 9, 514218, tzinfo=utc)),
        ),
    ]