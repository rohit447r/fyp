# Generated by Django 4.2.6 on 2023-10-19 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_rename_name_project_title_project_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2023, 10, 19, 23, 0, 53, 534211)),
        ),
    ]
