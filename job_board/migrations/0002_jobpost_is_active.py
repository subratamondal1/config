# Generated by Django 5.0.4 on 2024-04-18 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job_board", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobpost",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
