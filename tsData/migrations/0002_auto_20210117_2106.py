# Generated by Django 2.2.6 on 2021-01-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsData', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='company',
        ),
        migrations.AddField(
            model_name='measurementtag',
            name='company',
            field=models.CharField(blank=True, max_length=124, null=True),
        ),
        migrations.AlterField(
            model_name='measurementtag',
            name='plant',
            field=models.CharField(blank=True, max_length=124, null=True),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Plant',
        ),
    ]
