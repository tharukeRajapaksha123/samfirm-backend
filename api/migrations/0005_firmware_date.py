# Generated by Django 4.0 on 2022-01-02 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_firmware_headers'),
    ]

    operations = [
        migrations.AddField(
            model_name='firmware',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]