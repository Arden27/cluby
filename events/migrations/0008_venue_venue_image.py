# Generated by Django 4.1.2 on 2022-10-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0007_delete_myclubuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="venue",
            name="venue_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]