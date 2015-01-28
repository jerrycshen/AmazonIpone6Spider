# -*- coding: utf-8 -*-

# Scrapy settings for AmazonIphone6 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'AmazonIphone6'

SPIDER_MODULES = ['AmazonIphone6.spiders']
NEWSPIDER_MODULE = 'AmazonIphone6.spiders'

ITEM_PIPELINES = {
	'AmazonIphone6.pipelines.Amazoniphone6Pipeline' :300
}

COOKIES_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'AmazonIphone6 (+http://www.yourdomain.com)'
DOWNLOADER_MIDDLEWARES = {
	'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
     'AmazonIphone6.spiders.rotate_useragent.RotateUserAgentMiddleware' :400
}