# Generated by Django 5.0 on 2023-12-05 18:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=500)),
                ("division", models.CharField(max_length=500)),
            ],
            options={
                "db_table": "Teams",
            },
        ),
        migrations.AddField(
            model_name="eventclaim",
            name="team",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="dashboard.team",
            ),
        ),
    ]
