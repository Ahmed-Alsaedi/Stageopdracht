# Generated by Django 4.1.7 on 2023-02-22 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_data', '0002_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='cityCode',
            new_name='city_code',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='hotelNr',
            new_name='hotel_number',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='cityCode',
        ),
        migrations.AddField(
            model_name='hotel',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
