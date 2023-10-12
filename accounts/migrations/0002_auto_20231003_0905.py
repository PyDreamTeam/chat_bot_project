# Generated by Django 4.1.5 on 2023-10-03 09:05
from django.core.management import call_command
from django.db import migrations

from accounts.apps import AccountsConfig
from config.settings import BASE_DIR

fixture = BASE_DIR / "accounts/migrations/fixtures/solutionhistoryconfig.json"


def load_fixture(apps, schema_editor):
    call_command("loaddata", fixture, app_label=AccountsConfig.name)


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
