from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = CloudinaryField('profile_pictures', blank=True, null=True)  # ✅ Cloudinary

    is_journalist = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(default='content')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    image = CloudinaryField('article_images', blank=True, null=True)  # ✅ Cloudinary

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.article.title}"


class Advertisement(models.Model):
    title = models.CharField(max_length=250)
    image = CloudinaryField('ads', blank=True, null=True)  # ✅ Cloudinary
    url = models.URLField(default="https://google.com")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

