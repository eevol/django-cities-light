# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import cities_light.abstract_models


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0003_auto_20141120_0342'),
        ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_ascii', models.CharField(db_index=True, max_length=200, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'name_ascii', editable=False)),
                ('geoname_id', models.IntegerField(unique=True, null=True, blank=True)),
                ('alternate_names', models.TextField(default=b'', null=True, blank=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('display_name', models.CharField(max_length=200)),
                ('search_names', cities_light.abstract_models.ToSearchTextField(default=b'', max_length=4000, db_index=True, blank=True)),
                ('latitude', models.DecimalField(null=True, max_digits=8, decimal_places=5, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=8, decimal_places=5, blank=True)),
                ('population', models.BigIntegerField(db_index=True, null=True, blank=True)),
                ('feature_code', models.CharField(db_index=True, max_length=10, null=True, blank=True)),
                ],
            options={
                'ordering': ['name'],
                'abstract': False,
                'verbose_name_plural': 'communes',
                },
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'name_ascii', editable=False),
        ),
        migrations.AlterField(
            model_name='country',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'name_ascii', editable=False),
        ),
        migrations.AlterField(
            model_name='region',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'name_ascii', editable=False),
        ),
        migrations.AddField(
            model_name='commune',
            name='country',
            field=models.ForeignKey(to='cities_light.Country'),
        ),
        migrations.AddField(
            model_name='commune',
            name='region',
            field=models.ForeignKey(blank=True, to='cities_light.Region', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='commune',
            unique_together=set([('region', 'name'), ('region', 'slug')]),
        ),
        ]
