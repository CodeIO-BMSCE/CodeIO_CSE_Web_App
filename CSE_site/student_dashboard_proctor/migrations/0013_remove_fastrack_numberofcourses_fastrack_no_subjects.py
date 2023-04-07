# Generated by Django 4.1.3 on 2023-04-07 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "student_dashboard_proctor",
            "0012_remove_fastrackcourserequest_faculty_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fastrack",
            name="numberOfCourses",
        ),
        migrations.AddField(
            model_name="fastrack",
            name="no_subjects",
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]