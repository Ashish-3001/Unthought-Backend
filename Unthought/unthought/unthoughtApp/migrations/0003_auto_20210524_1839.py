# Generated by Django 3.0.5 on 2021-05-24 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unthoughtApp', '0002_individualchatlist_individualtext'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualchatlist',
            name='last_message',
            field=models.CharField(default='how are you ?', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='individualchatlist',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]