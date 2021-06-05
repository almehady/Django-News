from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.

STATUS_CHOICES = (
    ('D', 'Draft'),
    ('P', 'Published')
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
        primary_key=True,)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True) # user avatar upload

    def __str__(self):
        return self.user.email


class MainCategory(models.Model):
    title = models.CharField(max_length=200, blank=True, unique=True)
    slug = AutoSlugField(populate_from=title, editable=True, unique=True, unique_with=['created__month', 'status'])
    description = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    featured = models.BooleanField(help_text='Select this content for main menu', default=False)
    sequence = models.CharField(max_length=3, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='P')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created']
        verbose_name = 'Main Category'
        verbose_name_plural = 'Main Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('core:main-category-detail', args=[str(self.slug)])