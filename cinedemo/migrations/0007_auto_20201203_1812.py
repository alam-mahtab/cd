# Generated by Django 3.1.3 on 2020-12-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinedemo', '0006_inquiry_user_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='phone',
            field=models.IntegerField(max_length=20),
        ),
    ]