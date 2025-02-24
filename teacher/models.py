from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
