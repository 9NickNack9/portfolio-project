from django.db import models


class Job(models.Model):
    image = models.ImageField()
    summary = models.CharField(max_length=200)
