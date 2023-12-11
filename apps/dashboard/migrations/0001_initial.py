# Generated by Django 5.0 on 2023-12-05 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Athlete",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("firstName", models.CharField(max_length=500)),
                ("lastName", models.CharField(max_length=500)),
                (
                    "email",
                    models.CharField(
                        blank=True, default=None, max_length=500, null=True
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, default=None, max_length=500, null=True
                    ),
                ),
                (
                    "parent_id",
                    models.CharField(
                        blank=True, default=None, max_length=500, null=True
                    ),
                ),
                (
                    "parent_firstName",
                    models.CharField(
                        blank=True, default=None, max_length=500, null=True
                    ),
                ),
                (
                    "parent_lastName",
                    models.CharField(
                        blank=True, default=None, max_length=500, null=True
                    ),
                ),
                (
                    "parent_email",
                    models.CharField(
                        blank=True, default=None, max_length=500, null=True
                    ),
                ),
                (
                    "parent_phone",
                    models.CharField(
                        blank=True, default=None, max_length=500, null=True
                    ),
                ),
            ],
            options={
                "db_table": "Athletes",
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=500)),
                (
                    "partner",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="authentication.partner",
                    ),
                ),
            ],
            options={
                "db_table": "Events",
            },
        ),
        migrations.CreateModel(
            name="LeagueQuestions",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "question",
                    models.CharField(
                        blank=True, default=None, max_length=500, null=True
                    ),
                ),
                (
                    "answer",
                    models.CharField(
                        blank=True, default=None, max_length=500, null=True
                    ),
                ),
                (
                    "document",
                    models.CharField(
                        blank=True, default=None, max_length=500, null=True
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="dashboard.event",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="dashboard.athlete",
                    ),
                ),
            ],
            options={
                "db_table": "League Questions",
            },
        ),
        migrations.CreateModel(
            name="EventClaim",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("status", models.CharField(default="draft", max_length=100)),
                (
                    "event",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="dashboard.event",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="dashboard.athlete",
                    ),
                ),
                (
                    "league_questions",
                    models.ManyToManyField(to="dashboard.leaguequestions"),
                ),
            ],
            options={
                "db_table": "Event Claims",
            },
        ),
    ]