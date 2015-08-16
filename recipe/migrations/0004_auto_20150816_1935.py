# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20150816_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hop',
            name='stability',
            field=models.TextField(),
        ),
    ]
