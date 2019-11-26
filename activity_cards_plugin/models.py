from django.db import models
from cms.models.pluginmodel import CMSPlugin

# Create your models here.


class ActivityCard(CMSPlugin):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    image = models.ImageField(null=True, blank=True)
    link = models.CharField(max_length=100)
    
    ENGLISH = 'en'
    SPANISH = 'es'
    
    LANGUAGES = (
        (ENGLISH, 'en'),
        (SPANISH, 'es'),
    )
    lang = models.CharField(max_length=10, choices=LANGUAGES)
    
    def __str__(self):
        return "[{}] {}".format(self.lang, self.name)
