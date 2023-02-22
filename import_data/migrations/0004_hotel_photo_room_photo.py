# Generated by Django 4.1.7 on 2023-02-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_data', '0003_rename_citycode_city_city_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='photo',
            field=models.ImageField(default='Media/coming_soon.avif', upload_to='import_data/hotel_photos/'),
        ),
        migrations.AddField(
            model_name='room',
            name='photo',
            field=models.ImageField(default='Media/coming_soon.avif', upload_to='import_data/room_photos/'),
        ),
    ]