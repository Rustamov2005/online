# Generated by Django 5.0.7 on 2024-07-18 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 18, 15, 20, 34, 882692, tzinfo=datetime.timezone.utc)),
        ),
    ]
