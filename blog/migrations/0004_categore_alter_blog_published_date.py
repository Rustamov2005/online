# Generated by Django 5.0.7 on 2024-07-18 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_comments_alter_blog_published_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 18, 13, 6, 48, 559005, tzinfo=datetime.timezone.utc)),
        ),
    ]
