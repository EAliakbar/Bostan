# Generated by Django 2.1.1 on 2018-09-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offeredcourse',
            name='gender_spec',
            field=models.NullBooleanField(),
        ),
    ]
