# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_person_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=30)),
                ('publish_time', models.DateTimeField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('comment_time', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default='test@email.com', max_length=254),
            preserve_default=False,
        ),
    ]
