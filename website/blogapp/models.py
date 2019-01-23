from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext as _
from taggit.managers import TaggableManager
class BaseModel(models.Model):
    """ Base Model for all Models """
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modfied_at = models.DateTimeField(auto_now=True)
class Author(BaseModel):
    """ Author Model """
    email = models.EmailField(help_text=_("Email ID"))
    name = models.TextField(max_length=200, help_text=_("Name of the Author"))
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name
    
