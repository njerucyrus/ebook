# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-19 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20160819_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksissued',
            name='book_no',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
        ),
    ]
