# Generated by Django 3.1.3 on 2020-11-10 19:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('notes', '0011_auto_20201110_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newtaskform',
            name='creation_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='newtaskform',
            name='last_modified',
            field=models.DateTimeField(),
        ),
    ]
