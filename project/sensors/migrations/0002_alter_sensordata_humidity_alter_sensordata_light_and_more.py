# Generated by Django 5.0.4 on 2024-05-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='humidity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='light',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='rain',
            field=models.FloatField(),
        ),
    ]
