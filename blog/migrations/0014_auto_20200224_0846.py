# Generated by Django 3.0.3 on 2020-02-24 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200224_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='com_created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]