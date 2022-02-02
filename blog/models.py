from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, unique=True)
    parent = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cats': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Sophrologie')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    content = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='blog_posts'
    )

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse("article-detail", kwargs={'pk': self.pk})
        return reverse("home")
