# Generated by Django 5.0.4 on 2024-04-07 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="photo",
            field=models.ImageField(null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="client",
            name="date",
            field=models.DateField(default=datetime.date(2024, 4, 7)),
        ),
        migrations.AlterField(
            model_name="order",
            name="date",
            field=models.DateField(default=datetime.date(2024, 4, 7)),
        ),
        migrations.AlterField(
            model_name="product",
            name="date",
            field=models.DateField(default=datetime.date(2024, 4, 7)),
        ),
    ]