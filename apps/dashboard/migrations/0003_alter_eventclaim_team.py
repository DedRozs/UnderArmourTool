# Generated by Django 5.0 on 2023-12-05 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0002_team_eventclaim_team"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventclaim",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="dashboard.team",
            ),
        ),
    ]
