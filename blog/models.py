from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Commints(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user


class Blog(models.Model):
    class Status(models.TextChoices):
        PUBLISH = 'pb', 'Publish'
        DRAFT = 'ds', 'Draft'

    title = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField(upload_to="blog/blog")
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.PUBLISH)
    published_date = models.DateTimeField(default=timezone.now())
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Categore(models.Model):
    name = models.CharField(max_length=200)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name\




