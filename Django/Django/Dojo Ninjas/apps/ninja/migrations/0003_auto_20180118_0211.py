# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-18 02:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ninja', '0002_auto_20180118_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='ninja.Dojo'),
        ),
    ]
