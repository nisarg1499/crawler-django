from django.test import TestCase
from .models import Blogs, History, User

class BlogsTestCase(TestCase):
	def setUp(self):
		# creating objects with few fields only
		Blogs.objects.create(tag = "culture", title = "Title", content = "content1")
		Blogs.objects.create(tag = "tech", title = "Technology", content = "New content")

	def test_simple(self):
		object1 = Blogs.objects.get(tag = "culture")
		self.assertEqual(count(object1), 1)