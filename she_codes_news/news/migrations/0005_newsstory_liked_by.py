# Generated by Django 4.1.3 on 2022-12-18 06:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0004_alter_newsstory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='liked_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_stories', to=settings.AUTH_USER_MODEL),
        ),
    ]
