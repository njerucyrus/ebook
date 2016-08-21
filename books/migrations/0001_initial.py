# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-21 07:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_no', models.CharField(db_index=True, max_length=20, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('publisher', models.CharField(blank=True, max_length=100, null=True)),
                ('available', models.BooleanField(default=True)),
                ('date_recorded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('category_slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='BookCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('book_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='BooksIssued',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=13)),
                ('reg_no', models.CharField(max_length=20)),
                ('date_issued', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateField(auto_now_add=True)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='Book No')),
            ],
            options={
                'verbose_name_plural': 'Books Issued',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.BookCategory'),
        ),
    ]
