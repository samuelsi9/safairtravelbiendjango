# Generated by Django 4.1.7 on 2023-02-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='NOM',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='PRENOM',
            field=models.CharField(default='', max_length=50),
        ),
    ]