# Generated by Django 4.1.5 on 2023-12-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutionfilter',
            name='status',
            field=models.CharField(default='save', max_length=50),
        ),
        migrations.AddField(
            model_name='solutiongroup',
            name='status',
            field=models.CharField(default='save', max_length=50),
        ),
        migrations.AddField(
            model_name='solutiontag',
            name='status',
            field=models.CharField(default='save', max_length=50),
        ),
    ]