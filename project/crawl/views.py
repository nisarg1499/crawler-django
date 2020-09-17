# This view file contains functions of getting Blogs, getting history, crawl data

from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint
import scrapy
from scrapy.crawler import CrawlerProcess
import json, time
from scrapyd_api import ScrapydAPI
from scrapy import signals
from scrapy.crawler import Crawler, CrawlerProcess,CrawlerRunner
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import History, Blogs
# from django.contrib.auth import logout
from django.contrib.auth.models import User
from .trie import Trie
from django.db.models import Q


scrapyd = ScrapydAPI('http://127.0.0.1:6800')


# This function crawls the blogs from medium. But due to some issues crawler is not getting integrated and called from here.
@csrf_exempt
@login_required
def crawlBlogs(request):

	# get the tag from url
	tag = request.GET['tag']

	# call the crawler from scrape app
	task = scrapyd.schedule('default','medium',tag = tag)
	print(task)
	time.sleep(10)
	print('Done')
	return HttpResponse(201)

# This function gives all the blogs of a particular tag
### Please look on the actual function written at the bottom 
@login_required
def getBlogs(request,tag):

	# get the user details
	get_user = request.user
	user = User.objects.get(id = get_user.id)

	# define the filter based on tags
	filter = Q(tag__icontains = tag)
	# get the filtered datra from db
	filtered = Blogs.objects.filter(filter)

	# prepare history object
	history = History(user_id = user, 
					username = get_user.username,
					history = tag)

	# save data in db
	# all redundant searched will be stored, but can be further normalized and these data can be used to get analysis about how many times user searched the tag
	history.save()

	# show all blogs of a particular searched tag
	print(filtered.values())
	return HttpResponse('Blogs printed on console')

# This function shows history of searched tag
@login_required
def showHistory(request):

	# get user details
	get_user = request.user
	user = User.objects.get(id = get_user.id)

	# get filtered data on basis of user
	filtered = History.objects.filter(user_id = user).values('history')
	print('History')
	# print the history
	print(filtered.distinct())

	return HttpResponse('History displayed on console')



### Actual GetBlogs function
###
###

# @login_required
# def getBlogs(request,tag):

# 	get_user = request.user
# 	user = User.objects.get(id = get_user.id)

# 	filter = Q(tag__icontains = tag)
# 	filtered = Blogs.objects.filter(filter)

# 	if filtered == None:
# 		call suggest function of Trie
# 		Trie.suggest(tag)	
# 	else:
# 		if filtered[0].values('last_request') < 3 minutes:
# 			print(filtered.values())
# 		else:
# 			task = scrapyd.schedule('default','medium',tag = tag)
# 		history = History(user_id = user, 
# 						username = get_user.username,
# 						history = tag)

# 		history.save()
# 	return HttpResponse('Blogs printed on console')