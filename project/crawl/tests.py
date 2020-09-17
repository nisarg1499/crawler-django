from django.test import TestCase
from .models import Blogs, History, User
import datetime
from django.utils import timezone

class BlogsTestCase(TestCase):
	def setUp(self):
		# creating objects with few fields only
		d = datetime.datetime.now()
		Blogs.objects.create(tag = "culture", title = "Title", pusblish_date = '2020-09-17 20:44:28.433459', content = "content1")
		# Blogs.objects.create(tag = "tech", title = "Technology", pusblish_date = datetime(timezone.now), content = "New content")

	def test_simple(self):
		object1 = Blogs.objects.get(tag = "culture")
		self.assertEqual(count(object1), 1)