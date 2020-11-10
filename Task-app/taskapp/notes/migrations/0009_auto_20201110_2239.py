# Generated by Django 3.1.3 on 2020-11-10 18:39

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('notes', '0008_newtaskform_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newtaskform',
            old_name='time',
            new_name='creation_date',
        ),
        migrations.RenameField(
            model_name='newtaskform',
            old_name='task',
            new_name='task_description',
        ),
        migrations.AddField(
            model_name='newtaskform',
            name='last_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='newtaskform',
            name='task_title',
            field=models.TextField(default=datetime.datetime(2020, 11, 10, 18, 39, 21, 368819, tzinfo=utc),
                                   max_length=64),
            preserve_default=False,
        ),
    ]
