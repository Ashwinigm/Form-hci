# Generated by Django 3.2.7 on 2021-12-01 06:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0011_alter_newform_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newform',
            name='zipcode',
            field=models.CharField(max_length=5, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{5}$')]),
        ),
    ]
