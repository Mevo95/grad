from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group


class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    mobile_number = models.CharField(max_length=20, blank=True)
    birthday_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='users/', blank=True)
    posts = models.ManyToManyField('Post', related_name='user_posts', blank=True)
    comments = models.ManyToManyField('Comment', related_name='user_comments', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='movies_users')
    groups = models.ManyToManyField(Group, related_name='movies_users')

    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.content
