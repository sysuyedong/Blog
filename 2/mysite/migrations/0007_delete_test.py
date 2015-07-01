# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
    ]
