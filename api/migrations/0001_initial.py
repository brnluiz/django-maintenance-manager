# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('created_at', models.DateTimeField(verbose_name='created date')),
            ],
        ),
        migrations.CreateModel(
            name='Enquire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='created date')),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificator', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('reference', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(verbose_name='created date')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='api.Location')),
                ('enquire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Enquire')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificator', models.CharField(max_length=15)),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='api.Flat')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=70)),
                ('urgency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('created_at', models.DateTimeField(verbose_name='created date')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='api.Room')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='api.Status'),
        ),
        migrations.AddField(
            model_name='flat',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='api.Location'),
        ),
        migrations.AddField(
            model_name='enquire',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enquires', to='api.Room'),
        ),
        migrations.AddField(
            model_name='enquire',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enquires', to='api.Status'),
        ),
        migrations.AddField(
            model_name='enquire',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enquires', to='api.User'),
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='api.Role'),
        ),
    ]
