# Generated by Django 4.1.7 on 2023-04-23 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSE_site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='batch',
        ),
    ]