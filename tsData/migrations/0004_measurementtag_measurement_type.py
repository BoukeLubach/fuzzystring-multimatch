# Generated by Django 2.2.6 on 2021-01-17 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsData', '0003_auto_20210117_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurementtag',
            name='measurement_type',
            field=models.CharField(choices=[('flow', 'Flow'), ('temp', 'Temperature'), ('pres', 'Pressure'), ('pwr', 'Power'), ('level', 'Level'), ('oth', 'Other')], default='oth', max_length=5),
        ),
    ]
