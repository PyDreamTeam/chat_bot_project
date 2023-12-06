# Generated by Django 4.1.5 on 2023-11-13 16:36

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlatformFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('functionality', models.CharField(max_length=200, null=True)),
                ('integration', models.CharField(max_length=800, null=True)),
                ('multiple', models.BooleanField(default=True)),
                ('status', models.CharField(default='save', max_length=800)),
                ('image', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(default='save', max_length=800)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('properties', models.CharField(max_length=1000)),
                ('status', models.CharField(default='save', max_length=800)),
                ('image', models.TextField(blank=True, null=True)),
                ('is_message', models.BooleanField(default=False)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platforms.platformfilter')),
            ],
        ),
        migrations.AddField(
            model_name='platformfilter',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platforms.platformgroup'),
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.CharField(blank=True, max_length=200, null=True)),
                ('full_description', models.CharField(blank=True, max_length=800, null=True)),
                ('turnkey_solutions', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, default='save', max_length=800, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=800, null=True)),
                ('links_to_solution', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10000), blank=True, null=True, size=None)),
                ('filter', models.ManyToManyField(blank=True, null=True, to='platforms.platformtag')),
            ],
        ),
    ]
