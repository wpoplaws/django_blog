# Generated by Django 3.0.3 on 2020-02-14 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200213_1011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='data_dodania',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='opis',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='zdjecie',
            new_name='image',
        ),
    ]