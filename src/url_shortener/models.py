from django.db import models
import uuid
from hashlib import md5


class Link(models.Model):
    url = models.URLField(unique=True, max_length=10000)
    shorturl = models.CharField(unique=True, max_length=8)
    
    
    @classmethod
    def create(self, link):
        short = md5(link.encode()).hexdigest()[:8]
        try:
            obj = self.objects.create(url=link, shorturl=short)
        except:
            obj = self.objects.get(url=link)
        return obj