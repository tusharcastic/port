# Generated by Django 2.1.4 on 2019-01-21 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0017_port_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='port',
            name='add_cv',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
