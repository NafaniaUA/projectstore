# Generated by Django 3.1.2 on 2020-10-09 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storege', '0004_auto_20201009_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderr_connect_stor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storege.storege'),
        ),
    ]