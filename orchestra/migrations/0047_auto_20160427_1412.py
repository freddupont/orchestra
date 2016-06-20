# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import orchestra.models.communication.mixins
import orchestra.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestra', '0046_auto_20160426_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffingRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_deleted', models.BooleanField(default=False)),
                ('request_cause', models.IntegerField(choices=[(0, 'user'), (1, 'autostaff'), (2, 'restaff')])),
                ('project_description', models.TextField(blank=True, null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orchestra.Task')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orchestra.Worker')),
            ],
            options={
                'abstract': False,
            },
            bases=(orchestra.models.communication.mixins.StaffingRequestInquiryMixin, orchestra.utils.models.DeleteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='StaffingResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_deleted', models.BooleanField(default=False)),
                ('response_text', models.TextField(blank=True, null=True)),
                ('is_available', models.BooleanField()),
                ('is_winner', models.NullBooleanField()),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='orchestra.StaffingRequest')),
            ],
            options={
                'abstract': False,
            },
            bases=(orchestra.models.communication.mixins.StaffingResponseMixin, orchestra.utils.models.DeleteMixin, models.Model),
        ),
        migrations.AddField(
            model_name='communicationpreference',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='communicationpreference',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
