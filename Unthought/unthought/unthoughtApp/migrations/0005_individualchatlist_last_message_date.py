# Generated by Django 3.0.5 on 2021-05-24 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unthoughtApp', '0004_auto_20210524_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualchatlist',
            name='last_message_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
