# Generated by Django 4.0.dev20210713072537 on 2021-08-12 11:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_words_english_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 8, 12, 11, 4, 57, 892419, tzinfo=utc)),
        ),
    ]