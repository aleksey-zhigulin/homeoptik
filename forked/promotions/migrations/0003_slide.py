# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import oscar.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0002_auto_20150604_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('image', models.ImageField(upload_to=b'images/promotions/', max_length=255, verbose_name='Image')),
                ('link_url', oscar.models.fields.ExtendedURLField(help_text='This is where this promotion links to', verbose_name='Link URL', blank=True)),
                ('body', models.TextField(verbose_name='BxSlider text block in HTML')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slide',
            },
        ),
    ]
