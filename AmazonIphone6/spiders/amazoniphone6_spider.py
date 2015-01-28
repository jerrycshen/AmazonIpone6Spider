
    #/usr/bin/python
#-*-coding:utf-8-*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy import log

from AmazonIphone6.items import Amazoniphone6Item

class AmazonIphone6Spider(Spider):
	""" a spier of AmazonIphone6"""

	name = "AmazonIphone6"
	# set delay time 4s 
	download_delay = 6
	allowed_domains = ["amazon.cn"]
	# the first url
	start_urls = [
		"http://www.amazon.cn/s/ref=nb_sb_noss_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=node%3D665002051&field-keywords=iphone6&rh=n%3A664978051%2Cn%3A665002051%2Ck%3Aiphone6"
	]


	def parse(self,response):
		# check the url is a first url or not,because the first page is different from other pages
		sel = Selector(response)

		goods = sel.xpath("//li[@class='s-result-item']")

		# print goods


		for good in goods:

			# print good

			item = Amazoniphone6Item()
			
			good_name = good.xpath("div/div/div/a/h2/text()").extract()
		
			good_url = good.xpath("div/div/div/div/a/@href").extract()
			good_price = good.xpath("div/div/div/a[@class='a-link-normal a-text-normal']/span/text()").extract()
			good_star = good.xpath("div/div/span/span/a/i/span/text()").extract()

			good_commentsnum = good.xpath("div/div/a[@class='a-size-small a-link-normal a-text-normal']/text()").extract()
			good_commentsurl = good.xpath("div/div/a[@class='a-size-small a-link-normal a-text-normal']/@href").extract()


			item["good_name"] = [n.encode('utf-8') for n in good_name]
			item["good_url"] = [n.encode('utf-8') for n in good_url]
			item["good_price"] = [n.encode('utf-8') for n in good_price]
			item["good_star"] = [n.encode('utf-8') for n in good_star]
			item["good_commentsnum"] = [n.encode('utf-8') for n in good_commentsnum]
			item["good_commentsurl"] = [n.encode('utf-8') for n in good_commentsurl]

			yield item


		for url in sel.xpath("//a[@id='pagnNextLink']/@href").extract():
			yield Request("http://www.amazon.cn"+url,callback=self.parse)
		







		
