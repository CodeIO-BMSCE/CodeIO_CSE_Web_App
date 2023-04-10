# Generated by Django 4.0.8 on 2023-01-08 04:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('threads', '0004_thread_liked_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='dislike',
            field=models.ManyToManyField(blank=True, default=None, related_name='disliked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Dislikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Dislike', 'Dislike'), ('Undo', 'Undo')], default='Dislike', max_length=10)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threads.thread')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
