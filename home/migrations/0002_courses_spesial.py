# Generated by Django 5.0.7 on 2024-07-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='spesial',
            field=models.ManyToManyField(to='home.speciality'),
        ),
    ]
