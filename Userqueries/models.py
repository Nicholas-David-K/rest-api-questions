from django.db import models
from django.conf import settings

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='questions')
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='photo/%y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.content



class Answer(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='votes', blank=True, null=True)

    def __str__(self):
        return self.author.first_name
