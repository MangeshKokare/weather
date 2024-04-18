# Generated by Django 4.2.2 on 2024-02-26 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_weathersearchhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='weathersearchhistory',
            name='coordinate',
            field=models.CharField(default='8765', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='weathersearchhistory',
            name='country_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='weathersearchhistory',
            name='humidity',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='weathersearchhistory',
            name='pressure',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='weathersearchhistory',
            name='temperature',
            field=models.CharField(max_length=30),
        ),
    ]
