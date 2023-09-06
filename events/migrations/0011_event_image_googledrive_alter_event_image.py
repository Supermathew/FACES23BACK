# Generated by Django 4.2.4 on 2023-09-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0010_alter_event_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="image_googledrive",
            field=models.URLField(
                blank=True, null=True, verbose_name="Image Google Drive"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="uploads/", verbose_name="Event Banner"
            ),
        ),
    ]
