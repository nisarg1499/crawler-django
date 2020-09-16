import scrapy
from scrapy.crawler import CrawlerProcess
import json
from pprint import pprint

class BlogScrawler(scrapy.Spider):
	
	name = 'new'
	custom_settings = {
		'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
		'DOWNLOAD_DELAY': 1
	}

	def __init__(self, *args, **kwargs):
		print('Inside')
		self.tag = 'culture'
		self.start_urls = ['https://medium.com/tag/'+self.tag]

	def parse(self, response):
		for card in response.css('div[class="streamItem streamItem--postPreview js-streamItem"]'):
			# print('card')
			features = {
				'title' : card.css('h3[class="graf graf--h3 graf-after--figure graf--title"]::text').get(),
				'details_datetime' : card.css('time::attr(datetime)').get(),
				'details_readtime' : card.css('span[class="readingTime"]::attr(title)').get(),
				'link' : card.css('a[class="button button--smaller button--chromeless u-baseColor--buttonNormal"]::attr(href)').get(),
				'blog_content' : '',
				'tags' : ''
			}
			# pprint(features)
			yield response.follow(
				url = features['link'],
				# headers = self.headers,
				callback = self.parse_article,
				meta = {
					'blogs' : features
				}
			)

	def parse_article(self, response):
		article = response.meta.get('blogs')
		# print('done')
		# article['tags'] = response.css('div[class="rs s"]').getall()
		# print(article['tags'])
		article['blog_content'] = response.css('article[class="meteredContent"] *::text')
		article['blog_content'] = '\n'.join(article['blog_content'].getall())
		pprint(article)