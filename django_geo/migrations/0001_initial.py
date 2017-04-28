# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip_code', models.CharField(max_length=10, db_index=True)),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=6, db_index=True)),
                ('longitude', models.DecimalField(max_digits=10, decimal_places=6, db_index=True)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
    ]
