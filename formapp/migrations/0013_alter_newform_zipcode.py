# Generated by Django 3.2.7 on 2021-12-01 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0012_alter_newform_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newform',
            name='zipcode',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
