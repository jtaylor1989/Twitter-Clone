# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import tweets.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=255, validators=[tweets.validators.validate_content]),
        ),
    ]
