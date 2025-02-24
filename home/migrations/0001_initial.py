# Generated by Django 5.0.7 on 2024-07-18 09:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='speciality/')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='subjects/')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='teachers/')),
                ('social_link_telegram', models.URLField(null=True)),
                ('social_link_youtube', models.URLField(null=True)),
                ('social_link_linkedin', models.URLField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('students', models.IntegerField()),
                ('img', models.ImageField(upload_to='courses/')),
                ('price', models.FloatField()),
                ('rating', models.BooleanField()),
                ('mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.teachers')),
            ],
        ),
    ]
