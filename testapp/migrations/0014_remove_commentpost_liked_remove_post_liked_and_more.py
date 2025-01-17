# Generated by Django 5.0.1 on 2024-05-18 15:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0013_commentpost_created_at_commentpost_liked_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentpost',
            name='liked',
        ),
        migrations.RemoveField(
            model_name='post',
            name='liked',
        ),
        migrations.AlterField(
            model_name='likecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_comment_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='likepost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
