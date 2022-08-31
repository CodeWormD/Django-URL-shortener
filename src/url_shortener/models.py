import uuid
from hashlib import md5

from django.db import models


class Link(models.Model):
    url = models.URLField(unique=True, max_length=10000)
    shorturl = models.CharField(unique=True, max_length=8)
    
    
    @classmethod
    def create(cls, link):
        short = md5(link.encode()).hexdigest()[:8]
        try:
            obj = cls.objects.create(url=link, shorturl=short)
        except:
            obj = cls.objects.get(url=link)
        return obj
