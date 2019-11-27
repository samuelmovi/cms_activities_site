from django.contrib import admin
from cms.extensions import PageExtensionAdmin

# Register your models here.
from .models import CategoryExtension


class CategoryExtensionAdmin(PageExtensionAdmin):
    pass


admin.site.register(CategoryExtension, CategoryExtensionAdmin)
