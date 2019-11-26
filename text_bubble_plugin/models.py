from django.db import models
from cms.models.pluginmodel import CMSPlugin


# Create your models here.
class TextModel(CMSPlugin):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return f'[{self.title}]'
