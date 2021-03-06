# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-20 11:11
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128, verbose_name='\u0424\u0418\u041e')),
                ('avatar', models.ImageField(blank=True, upload_to=b'avatars')),
                ('total_order_sum', models.FloatField(default=0.0, verbose_name='\u0418\u0442\u043e\u0433\u043e \u0437\u0430\u043a\u0430\u0437\u0430\u043d\u043e \u043d\u0430 \u0441\u0443\u043c\u043c\u0443')),
                ('total_order_count', models.IntegerField(default=0, verbose_name='\u0418\u0442\u043e\u0433\u043e \u0437\u0430\u043a\u0430\u0437\u043e\u0432')),
                ('phone_number', models.CharField(blank=True, max_length=11, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430')),
                ('email', models.EmailField(max_length=254, verbose_name='\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u044b\u0439 \u0430\u0434\u0440\u0435\u0441')),
                ('date_joined', models.DateField(default=datetime.datetime(2016, 3, 20, 11, 11, 57, 496100, tzinfo=utc), verbose_name='\u0414\u0430\u0442\u0430 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438')),
                ('status', models.CharField(choices=[('\u041d\u043e\u0432\u0438\u0447\u043e\u043a', '\u041d\u043e\u0432\u0438\u0447\u043e\u043a'), ('\u041b\u044e\u0431\u0438\u0442\u0435\u043b\u044c', '\u041b\u044e\u0431\u0438\u0442\u0435\u043b\u044c'), ('\u0413\u0443\u0440\u043c\u0430\u043d', '\u0413\u0443\u0440\u043c\u0430\u043d'), ('\u0421\u0443\u0448\u0438\u043c\u0435\u043d', '\u0421\u0443\u0448\u0438\u043c\u0435\u043d')], default='\u041d\u043e\u0432\u0438\u0447\u043e\u043a', max_length=10, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f')),
                ('about', models.TextField(blank=True, verbose_name='\u041e \u0441\u0435\u0431\u0435')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
