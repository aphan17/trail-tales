# Generated by Django 4.2.2 on 2023-06-13 16:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0003_alter_post_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="length",
            new_name="hike_length",
        ),
    ]
