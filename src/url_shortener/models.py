from django.db import models


class Link(models.Model):
    url = models.CharField(max_length=10000)
    shorturl = models.CharField(max_length=10)