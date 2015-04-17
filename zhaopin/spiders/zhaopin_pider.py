# -*- coding: utf-8 -*-
__author__ = 'xiaoheng'

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from zhaopin.items import JobItem
import re
import string
import MySQLdb

class CitySpider(Spider):
    name = "zhaopin"
    allowed_domains = ["zhaopin.com"]
    start_urls = [
        "http://jobs.zhaopin.com/pd1/p1"
    ]
    
    def __init__(self, name=None, **kwargs):
        Spider.__init__(self, name, **kwargs)
        self.db = MySQLdb.connect(host="localhost",
            user="root",
            passwd="12345689",
            db="zhaopin",
            charset='utf8')                         
        self.cursor = self.db.cursor()


    def parse(self, response):
        sel = Selector(response)
        sites_error = sel.xpath('//div[@class="no-resulte-warning"]').extract()
        if not sites_error:
            current_url = response._get_url()
            pattern = ".*/pd1/p(.*)"
            match_num = re.search(pattern, current_url, re.M | re.I)
            num = string.atoi(match_num.group(1)) + 1
            next_url = "http://jobs.zhaopin.com/pd1/p" + str(num)
            yield Request(next_url, callback=self.parse)    #return the request of the next page's
            
            sites_url = sel.xpath('//span[@class="search_list_zw search_list_first"]/a')
            #pider the url of job's and return the request of the url's
            for site in sites_url:
                url = site.xpath('@href').extract()
                # sql = "select count(*) from job where url='%s'" % url[0]
                # self.cursor.execute(sql)
                # data = self.cursor.fetchone()
                # if data[0] == 0:
                yield Request(url[0], callback=self.my_parse)
                # else:
                #     print "it is chongfu : %s" % url[0]

    def my_parse(self, response):
        sel = Selector(response)
        item_job = JobItem()

        item_job["url"]        = response._get_url()[:-8]
        #item_job["name"]       = sel.xpath('//div[@class="inner-left fl"]/h1/text()').extract()
        item_job["name"]       = [n.encode('utf-8') for n in sel.xpath('//div[@class="inner-left fl"]/h1/text()').extract()]
        item_job["company"]    = [n.encode('utf-8') for n in sel.xpath('//div[@class="inner-left fl"]/h2/a/text()').extract()]
        item_job["com_url"]    = [n.encode('utf-8') for n in sel.xpath('//div[@class="inner-left fl"]/h2/a/@href').extract()]
        item_job["welfare"]    = [n.encode('utf-8') for n in sel.xpath('//div[@class="inner-left fl"]/div/span/text()').extract()]

        sites = sel.xpath('//ul[@class="terminal-ul clearfix"]/li')
        item_job["mon_pay"]    = [n.encode('utf-8') for n in sites[0].xpath('./strong/text()').extract()]
        item_job["place"]      = [n.encode('utf-8') for n in sites[1].xpath('./strong/a/text()').extract()]
        item_job["sub_place"]  = [n.encode('utf-8') for n in sites[1].xpath('./strong/text()').extract()]
        item_job["date"]       = [n.encode('utf-8') for n in sites[2].xpath('./strong/span/text()').extract()]
        item_job["job_prop"]   = [n.encode('utf-8') for n in sites[3].xpath('./strong/text()').extract()]
        item_job["exper"]      = [n.encode('utf-8') for n in sites[4].xpath('./strong/text()').extract()]
        item_job["edu"]        = [n.encode('utf-8') for n in sites[5].xpath('./strong/text()').extract()]
        item_job["num"]        = [n.encode('utf-8') for n in sites[6].xpath('./strong/text()').extract()]
        item_job["classify"]   = [n.encode('utf-8') for n in sites[7].xpath('./strong/a/text()').extract()]

        sites = sel.xpath('//div[@class="tab-inner-cont"]')
        item_job["descr"]       = [n.encode('utf-8') for n in sites[0].xpath('.//*/text()').extract()]
        item_job["com_intro"]  = [n.encode('utf-8') for n in sites[1].xpath('.//*/text()').extract()[2:]]

        sites = sel.xpath('//div[@class="company-box"]')
        #item_job["com_url"]    = [n.encode('utf-8') for n in sites.xpath('./p/a/@href').extract()]
        #item_job["com_name"]   = [n.encode('utf-8') for n in sites.xpath('./p/a/text()').extract()]

        sites = sites.xpath('./ul/li')
        item_job["com_scale"]  = [n.encode('utf-8') for n in sites[0].xpath('./strong/text()').extract()]
        item_job["com_prop"]   = [n.encode('utf-8') for n in sites[1].xpath('./strong/text()').extract()]
        item_job["com_indust"] = [n.encode('utf-8') for n in sites[2].xpath('./strong/a/text()').extract()]
        item_job["com_dress"]  = [n.encode('utf-8') for n in sites[-1].xpath('./strong/text()').extract()]

        if sites[3] != sites[-1]:
            item_job["com_home"]  = [n.encode('utf-8') for n in sites[3].xpath('./strong/a/text()').extract()]
        else:
            item_job["com_home"]  = [n.encode('utf-8') for n in ["null"]]

        return item_job
