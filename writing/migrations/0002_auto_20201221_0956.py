# Generated by Django 3.1.4 on 2020-12-21 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='text',
            new_name='description',
        ),
    ]
