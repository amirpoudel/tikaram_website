# Generated by Django 3.1.5 on 2021-02-12 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='report_file',
            new_name='files',
        ),
    ]