import scrapy
from scrapy.crawler import CrawlerProcess
import json

class BlogScrawler(scrapy.Spider):
	
	name = 'medium'

	def __init__(self, *args, **kwargs):
		print('Inside')
		self.tag = 'culture'
		self.start_urls = ['https://medium.com/tag/'+self.tag]

	def parse(self, response):
		for card in response.css('div[class="streamItem streamItem--postPreview js-streamItem"]'):
			features = {
				'title' : card.css('h3[class="graf graf--h3 graf-after--figure graf--title"]::text').get(),
				'details_datetime' : card.css('time::attr(datetime)').get(),
				'details_readtime' : card.css('span[class="readingTime"]::attr(title)').get(),
				'link' : card.css('a[class="button button--smaller button--chromeless u-baseColor--buttonNormal"]::attr(href)').get(),
				'blog_content' : '',
				'tags' : ''
			}

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

		# article['tags'] = response.css('div[class="rs s"]').getall()
		# print(article['tags'])
		article['blog_content'] = response.css('article[class="meteredContent"] *::text')
		article['blog_content'] = '\n'.join(article['blog_content'].getall())
		print(article)