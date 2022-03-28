from django.db import models
from tinymce.models import HTMLField
# Create your models here.
from users.models import CustomUser
from django.utils import timezone


class Categories(models.Model):
    cat_name = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='posts/categories/thumbnails/', default='none')

    def __str__(self):
        return self.cat_name


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_cat = models.ForeignKey(Categories, on_delete=models.CASCADE)
    post_img = models.ImageField(upload_to='posts/images/')
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

