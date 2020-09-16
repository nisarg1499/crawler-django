from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint
import scrapy
from scrapy.crawler import CrawlerProcess
import json, time
from scrapyd_api import ScrapydAPI
from scrapy import signals
from scrapy.crawler import Crawler, CrawlerProcess,CrawlerRunner
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import History
from django.contrib.auth import logout
from django.contrib.auth.models import User

scrapyd = ScrapydAPI('http://127.0.0.1:6800')

@csrf_exempt
def crawlBlogs(request):
	tag = request.GET['tag']

	task = scrapyd.schedule('default','medium',tag = tag)
	print(task)
	time.sleep(10)
	print('Done')
	return HttpResponse(201)


@login_required
def getBlogs(request):

	tag = request.GET['tag']
	get_user = request.user
	user = User.objects.get(id = get_user.id)
	print(get_user.id)
	print(get_user.username)

	history = History(user_id = user, 
					username = get_user.username,
					history = tag)

	# print(history)
	history.save()
	print('History saved')
	# logout(request)
	return HttpResponse(201)


@login_required
def showHistory(request):

	get_user = request.user
	user = User.objects.get(id = get_user.id)

	filtered = History.objects.filter(user_id = user).values('history')
	print('History')
	print(filtered.distinct())

	return HttpResponse('History displayed on console')



