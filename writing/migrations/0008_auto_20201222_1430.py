# Generated by Django 3.1.4 on 2020-12-22 21:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0007_auto_20201222_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 12, 22, 14, 30, 21, 456871), null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='parent',
            field=models.TextField(default='Talent is Never Enough'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.TextField(default='Exercise'),
        ),
    ]
