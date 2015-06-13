# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy

class JobItem(scrapy.Item):
    # define the fields for your item here like:
    url         = scrapy.Field()
    name        = scrapy.Field()
    company     = scrapy.Field()    #公司
    welfare     = scrapy.Field()    #待遇
    mon_pay     = scrapy.Field()    #月薪
    place       = scrapy.Field()    #工作地点
    sub_place   = scrapy.Field()    #子工作地点
    # date        = scrapy.Field()    #发布日期
    job_prop    = scrapy.Field()    #工作性质
    exper       = scrapy.Field()    #工作经验
    edu         = scrapy.Field()    #最低学历
    num         = scrapy.Field()    #招聘人数
    classify    = scrapy.Field()    #职位类别
    descr       = scrapy.Field()    #置位描述

    com_url         = scrapy.Field()
    com_name        = scrapy.Field()
    com_scale       = scrapy.Field()  #规模
    com_prop        = scrapy.Field()  #公司性质
    com_indust      = scrapy.Field()  #公司行业
    com_home        = scrapy.Field()  #公司主页
    com_dress       = scrapy.Field()  #公司地址
    com_intro       = scrapy.Field()  #公司介绍