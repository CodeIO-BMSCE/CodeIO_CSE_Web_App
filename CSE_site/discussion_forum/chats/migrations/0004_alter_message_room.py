# Generated by Django 4.0.8 on 2022-12-17 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_alter_message_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=25),
        ),
    ]
