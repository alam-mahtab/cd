# Generated by Django 3.1.3 on 2020-12-04 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinedemo', '0007_auto_20201203_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='CD_Id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
