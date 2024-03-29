# Generated by Django 4.2.5 on 2023-10-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
                ('joptitle', models.CharField(blank=True, max_length=30, null=True)),
                ('location', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('education', models.CharField(max_length=20, null=True)),
                ('describtion', models.CharField(max_length=20, null=True)),
                ('skils', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
                ('work_experience', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CS', models.CharField(blank=True, max_length=30, null=True)),
                ('marketing', models.CharField(max_length=20, null=True)),
                ('accounting', models.CharField(max_length=20, null=True)),
                ('engineering', models.CharField(max_length=20, null=True)),
                ('judiciary', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='jop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salay', models.IntegerField(null=True)),
                ('describtion', models.CharField(max_length=20, null=True)),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('location', models.CharField(max_length=40, null=True)),
            ],
        ),
    ]
