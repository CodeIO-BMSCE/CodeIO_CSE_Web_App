# Generated by Django 4.1.7 on 2023-04-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_cie_allocator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assigned_exam_room',
            name='room_name',
        ),
        migrations.AddField(
            model_name='assigned_exam_room',
            name='room_number',
            field=models.IntegerField(null=True),
        ),
    ]
