# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-14 16:14
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('original', easy_thumbnails.fields.ThumbnailerImageField(default='/tmp/none.jpg', upload_to=b'gallery')),
                ('description', models.CharField(blank=True, max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
