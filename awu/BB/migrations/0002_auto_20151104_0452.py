# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BB', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='ordering',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='forum',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='forum',
            name='slug',
            field=models.SlugField(max_length=120),
        ),
    ]
