# Generated by Django 5.1.4 on 2025-01-08 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0001_initial'),
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='current_location',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='destination',
        ),
        migrations.AddField(
            model_name='complaint',
            name='route_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='routes.route'),
        ),
    ]
