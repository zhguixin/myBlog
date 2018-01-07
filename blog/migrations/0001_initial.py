# -*- coding: UTF-8 -*-
# Generated by Django 2.1 on 2018-01-04 02:48

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
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('author', models.CharField(max_length=16, verbose_name='作者')),
                ('content', models.TextField(verbose_name='博客正文')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
        ),
    ]
