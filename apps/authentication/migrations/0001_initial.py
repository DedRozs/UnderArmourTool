# Generated by Django 5.0 on 2023-12-05 16:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Partner",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Permission",
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
                (
                    "feature",
                    models.CharField(
                        choices=[
                            ("Edit User", "Edit"),
                            ("Email", "Email"),
                            ("DOB", "Dob"),
                            ("Account Type", "Accounttype"),
                            ("Parent ID", "Parentid"),
                            ("Event Claim Inquiry", "Eventclaiminq"),
                        ],
                        max_length=100,
                    ),
                ),
                ("allowed", models.BooleanField(default=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "Permissions",
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("usertype", models.CharField(default="User", max_length=20)),
                (
                    "partner",
                    models.ManyToManyField(
                        blank=True,
                        default=None,
                        related_name="allowed_partners",
                        to="authentication.partner",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "UserProfiles",
            },
        ),
    ]