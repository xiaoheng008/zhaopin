# -*- coding: utf-8 -*-

# Scrapy settings for zhaopin project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'zhaopin'

SPIDER_MODULES = ['zhaopin.spiders']
NEWSPIDER_MODULE = 'zhaopin.spiders'

ITEM_PIPELINES = {  
    'zhaopin.pipelines.ZhaopinPipeline':300  
}
COOKIES_ENABLES=False

CONCURRENT_REQUESTS 			= 16	
CONCURRENT_REQUESTS_PER_DOMAIN 	= 12

DOWNLOADER_MIDDLEWARES = {
	'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None, 
	'zhaopin.my_useragent.MyUserAgentMiddleware' : 400
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhaopin (+http://www.yourdomain.com)'