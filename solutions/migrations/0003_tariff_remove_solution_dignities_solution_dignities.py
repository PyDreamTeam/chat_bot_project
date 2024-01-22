# Generated by Django 4.1.5 on 2024-01-22 17:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0002_solutionfilter_status_solutiongroup_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_special', models.CharField(blank=True, max_length=100, null=True)),
                ('tags_of_rates', models.JSONField()),
            ],
        ),
        migrations.RemoveField(
            model_name='solution',
            name='dignities',
        ),
        migrations.AddField(
            model_name='solution',
            name='dignities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10000), blank=True, null=True, size=None),
        ),
    ]