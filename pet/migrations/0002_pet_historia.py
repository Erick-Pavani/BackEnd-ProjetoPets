# Generated by Django 4.0.5 on 2022-06-05 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pet", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pet",
            name="historia",
            field=models.TextField(default=None),
        ),
    ]