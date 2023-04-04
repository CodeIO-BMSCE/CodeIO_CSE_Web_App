# Generated by Django 4.1.3 on 2023-04-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_dashboard_proctor', '0002_alter_student_options_remove_student_usn_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='student',
            name='USN',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
