from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext as _
from taggit.managers import TaggableManager


class BaseModel(models.Model):
    """ Base Model for all Models """
    active = models.BooleanField(default=True, help_text=_("Active?"))
    created_at = models.DateTimeField(auto_now_add=True)
    modfied_at = models.DateTimeField(auto_now=True)


class Author(BaseModel):
    """ Author Model """
    email = models.EmailField(help_text=_("Email ID"))
    name = models.TextField(max_length=200, help_text=_("Name of the Author"))
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)


class Category(BaseModel):
    """ Categories Model """
    created_by = models.ForeignKey(
        Author,
        on_delete=models.SET(1),
        related_name="created_categories",
        help_text=_("Created User Name"))
    name = models.TextField(max_length=200, unique=True, help_text=_("Category Name"))
    slug = models.SlugField(unique=True)

    class Meta:        
        verbose_name_plural = 'Catagories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Article(BaseModel):
    """ Article Model """    
    cat = models.ForeignKey(
        Category, on_delete=models.SET(1),
        related_name="articles", help_text=_("Article Category"))    
    content = models.TextField(help_text=_("Content"))
    created_by = models.ForeignKey(Author, on_delete=models.SET(1), related_name="articles")
    draft = models.BooleanField(default=True, help_text=_("Draft"))
    published_date = models.DateTimeField(help_text=_("Article Published Date"))
    read_time = models.CharField(max_length=100, blank=True, null=True)
    title = models.TextField(
        max_length=300, unique_for_date=published_date,
        help_text="Article Title")
    slug = models.SlugField(unique_for_date=published_date)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

