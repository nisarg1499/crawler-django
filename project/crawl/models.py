from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Blogs(models.Model):
	tag = models.TextField()
	title = models.TextField()
	published_date = models.DateTimeField()
	read_time = models.TextField()
	link = models.TextField()
	content = models.TextField()
	last_request = models.DateTimeField()

class History(models.Model):
	user_id = models.ForeignKey(User, on_delete = models.CASCADE)
	username = models.TextField()
	history = models.TextField()
	searched_time = models.DateTimeField(default = timezone.now)