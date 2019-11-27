from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool


class CategoryExtension(PageExtension):
    category = models.CharField(max_length=25)


extension_pool.register(CategoryExtension)
