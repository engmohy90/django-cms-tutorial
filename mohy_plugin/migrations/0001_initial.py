# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_Specials',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='mohy_plugin_daily_specials', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=b'daily_specials')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Daily Special',
                'verbose_name_plural': 'Daily Special',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
