# Generated by Django 4.2.5 on 2023-11-23 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0006_rename_cs_department_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='cvs',
        ),
    ]
