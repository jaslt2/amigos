# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.Location'),
        ),
    ]