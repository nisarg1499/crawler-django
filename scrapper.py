import scrapy
from scrapy.crawler import CrawlerProcess
import json

class ArticleScraper(scrapy.Spider):
	name = 'articles'

	headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }

	custom_settings = {
		'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
		'DOWNLOAD_DELAY': 1
	}

	def start(self):
		base_url = 'https://medium.com/tag/culture'
		# base_url = base_url + tag
		yield scrapy.Request(
			url = self.base_url,
			headers = self.headers,
			callback = self.parse_cards
		)

	def parse_cards(self, response):

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
				headers = self.headers,
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
		# print(json.dumps(article, indent = 2))

		with open(article['title'], 'w') as f:
			f.write(
				article['title'] + '\n' + 
				article['details_datetime'] + '\n' +
				article['details_readtime'] + '\n' + 
				article['link'] + '\n\n\n' + 
				article['blog_content']
			)


if __name__ == '__main__':
	# tag = 'culture'
	process = CrawlerProcess()
	process.crawl(ArticleScraper)
	# print('Process start')
	process.start()
