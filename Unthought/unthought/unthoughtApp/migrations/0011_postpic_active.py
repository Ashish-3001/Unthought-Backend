# Generated by Django 3.0.5 on 2021-05-10 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unthoughtApp', '0010_auto_20210510_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpic',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
