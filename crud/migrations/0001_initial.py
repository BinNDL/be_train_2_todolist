# Generated by Django 4.2.7 on 2023-12-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Scheduled", "Scheduled"),
                            ("On Track", "On Track"),
                            ("Off Track", "Off Track"),
                            ("In Jeopardy", "In Jeopardy"),
                            ("Complete", "Complete"),
                            ("Closed", "Closed"),
                        ],
                        default="Scheduled",
                        max_length=20,
                    ),
                ),
            ],
            options={
                "db_table": "task",
            },
        ),
    ]
