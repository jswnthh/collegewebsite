from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=100, default="Anonymous")
    excerpt = models.TextField(blank=True)
    content = CKEditor5Field('Text', config_name='extends')

    image = models.ImageField(
        upload_to="blog_images/",
        default="blog_images/blog_default.jpg",
        blank=True
    )

    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
