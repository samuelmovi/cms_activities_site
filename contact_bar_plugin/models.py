from cms.models.pluginmodel import CMSPlugin
from django.db import models

# Create your models here.


class Contact(CMSPlugin):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    
    def __str__(self):
        return f'[{self.name}][{self.link}][{self.text}]'

