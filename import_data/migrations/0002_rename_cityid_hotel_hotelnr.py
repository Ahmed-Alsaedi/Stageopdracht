# Generated by Django 4.1.5 on 2023-01-16 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='cityID',
            new_name='hotelNr',
        ),
    ]
