# Generated by Django 4.2.5 on 2023-11-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0011_rename_age_applicant_birthdate_applicant_cvl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='birthdate',
            field=models.DateField(null=True),
        ),
    ]
