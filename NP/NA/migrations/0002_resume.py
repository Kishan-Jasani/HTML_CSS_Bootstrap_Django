# Generated by Django 3.1.2 on 2020-10-11 09:06

import NA.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='documents/%Y/%m/%d', validators=[NA.validators.validate_file_extension])),
            ],
        ),
    ]