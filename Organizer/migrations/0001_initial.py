# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('abbreviation', models.CharField(unique=True, max_length=10, verbose_name=b'Abbreviation')),
                ('limited', models.BooleanField(default=False, verbose_name=b'User-Restricted')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClientNotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(verbose_name=b'Note')),
                ('client', models.ForeignKey(to='Organizer.Client')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('client', models.ForeignKey(to='Organizer.Client')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPriority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('sort_order', models.IntegerField(default=99, verbose_name=b'Sort Order')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(verbose_name=b'Title')),
                ('notes', models.TextField(default=b'', verbose_name=b'Notes', blank=True)),
                ('due', models.DateTimeField(default=None, null=True, verbose_name=b'Due Date', blank=True)),
                ('project', models.ForeignKey(to='Organizer.Project')),
            ],
        ),
        migrations.CreateModel(
            name='TaskSeverity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('sort_order', models.IntegerField(default=99, verbose_name=b'Sort Order')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='severity',
            field=models.ForeignKey(to='Organizer.TaskSeverity'),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.ForeignKey(to='Organizer.ProjectPriority'),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
