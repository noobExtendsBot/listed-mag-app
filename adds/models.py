from django.db import models
from users.models import CustomUser
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.


class Add(models.Model):
    title = models.CharField(max_length=100, default='no title')
    thumbnail = models.ImageField(upload_to='adds/images/')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    link = models.CharField(max_length=500)
    priority = models.IntegerField(validators=[MinValueValidator(1)], unique=True)
    published_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

