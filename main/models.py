from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
	group_name = models.CharField(max_length=30)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.group_name

class Message(models.Model):
	group_belong = models.ForeignKey(Group, on_delete=models.CASCADE)
	content = models.CharField(max_length=1024)
	time_sent = models.DateTimeField(auto_now_add=True)
	sender = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.content[:30] + '...'


