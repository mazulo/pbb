# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('url', models.URLField(unique=True)),
                ('feed_url', models.URLField(null=True)),
                ('working', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
