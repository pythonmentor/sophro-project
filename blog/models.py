from django.db import models
from django.conf import settings
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def  __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # return reverse("article-detail", kwargs={'pk': self.pk})
        return reverse("home")
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Sophrologie')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='blog_posts')
    
    def total_likes(self):
        return self.likes.count()
    
    def  __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse("article-detail", kwargs={'pk': self.pk})
        return reverse("home")