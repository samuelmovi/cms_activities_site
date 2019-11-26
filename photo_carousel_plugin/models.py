from django.db import models
from cms.models.pluginmodel import CMSPlugin


# Create your models here.
class CarouselPhoto(CMSPlugin):
    name = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.name
