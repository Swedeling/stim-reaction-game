# Generated by Django 4.0.4 on 2022-05-22 08:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_rename_scores_score_alter_game_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 22, 8, 28, 49, 884429, tzinfo=utc)),
        ),
    ]
