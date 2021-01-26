from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-home')


class PostComment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name ='comments')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField(max_length=1000, blank=True, null=True)
	created_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.content) if self.content else ''