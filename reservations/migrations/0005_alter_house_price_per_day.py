# Generated by Django 5.0.6 on 2024-06-08 19:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reservations", "0004_alter_order_arrive_date_alter_order_exit_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="house",
            name="price_per_day",
            field=models.IntegerField(),
        ),
    ]
