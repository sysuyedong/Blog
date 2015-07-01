# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20150623_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(default='', to='mysite.Person'),
            preserve_default=False,
        ),
    ]
