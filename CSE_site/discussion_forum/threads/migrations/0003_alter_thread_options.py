# Generated by Django 4.0.8 on 2023-01-05 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0002_alter_thread_body_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-id']},
        ),
    ]
