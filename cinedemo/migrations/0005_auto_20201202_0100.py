# Generated by Django 3.1.3 on 2020-12-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinedemo', '0004_auto_20201202_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlight',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='schedule2',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='schedule3',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]