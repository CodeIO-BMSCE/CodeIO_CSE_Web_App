# Generated by Django 4.1.7 on 2023-04-10 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_cie_allocator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='id',
        ),
        migrations.AlterField(
            model_name='room',
            name='roomName',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
