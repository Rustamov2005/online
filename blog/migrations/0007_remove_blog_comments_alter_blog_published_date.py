# Generated by Django 5.0.7 on 2024-07-19 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='comments',
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 19, 17, 8, 19, 913847, tzinfo=datetime.timezone.utc)),
        ),
    ]
