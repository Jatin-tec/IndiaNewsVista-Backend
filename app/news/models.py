from django.db import models

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

class News(models.Model):
    author = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    source_id = models.CharField(max_length=200, null=True, blank=True)
    source_name = models.CharField(max_length=200, null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200, null=True, blank=True)

    content = MarkdownField(rendered_field='content_rendered', validator=VALIDATOR_STANDARD)
    content_rendered = RenderedMarkdownField()

    image_url = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_at']

class Categories(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.CharField(max_length=200, null=True, blank=True)
    value = models.CharField(max_length=200, null=True, blank=True)

    default_fetch = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(" ", "-").lower()
        super(Categories, self).save(*args, **kwargs)