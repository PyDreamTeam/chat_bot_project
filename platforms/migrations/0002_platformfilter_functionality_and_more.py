# Generated by Django 4.1.5 on 2023-07-27 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platforms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformfilter',
            name='functionality',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='platformfilter',
            name='integration',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='platformfilter',
            name='multiple',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='image',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='platformfilter',
            name='image',
            field=models.CharField(max_length=800, null=True),
        ),
    ]