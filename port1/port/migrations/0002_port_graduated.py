# Generated by Django 2.1.4 on 2019-01-16 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='port',
            name='graduated',
            field=models.BooleanField(default=True),
        ),
    ]
