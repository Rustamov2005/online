from django.db import models


class Subjects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='subjects/')

    def __str__(self):
        return self.title


class Teachers(models.Model):
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='teachers/')
    social_link_telegram = models.URLField(null=True)
    social_link_youtube = models.URLField(null=True)
    social_link_linkedin = models.URLField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.full_name


class Speciality(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='speciality/')
    created = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title


class Courses(models.Model):
    title = models.CharField(max_length=100)
    students = models.IntegerField()
    mentor = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=True)
    img = models.ImageField(upload_to='courses/')
    price = models.FloatField()
    rating = models.BooleanField()
    spesial = models.ManyToManyField(Speciality)

    def __str__(self):
        return self.title













