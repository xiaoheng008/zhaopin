# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
#from scrapy.exceptions import DropItem

class ZhaopinPipeline(object):
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost",
                                  user="root",
                                  passwd="12345689",
                                  db="zhaopin",
                                  charset='utf8')
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def process_item(self, item, spider):
        url             = ""
        name            = ""
        company         = ""
        welfare         = ""
        mon_pay         = ""
        mon_pay_down    = 0
        mon_pay_up      = 0
        place           = ""
        sub_place       = ""
        job_prop        = ""
        exper           = ""
        edu             = ""
        num             = ""
        classify        = ""
        descr           = ""
        com_url         = ""
        com_scale       = ""
        com_prop        = ""
        com_indust      = ""
        com_home        = ""
        com_dress       = ""
        com_intro       = ""

        url             = item["url"]

        for ite in item["name"]:
            name 		+= ite
        for ite in item["company"]:
            company 	+= ite
        for ite in item["welfare"]:
            welfare 	+= ite + " "
        for ite in item["mon_pay"]:
            mon_pay		+= ite
        for ite in item["place"]:
            place 		+= ite
        for ite in item["sub_place"]:
            sub_place 	+= ite
        for ite in item["job_prop"]:
            job_prop 	+= ite
        for ite in item["exper"]:
            exper 		+= ite
        for ite in item["edu"]:
            edu 		+= ite
        for ite in item["num"]:
            num			+= ite
        for ite in item["classify"]:
            classify	+= ite
        for ite in item["descr"]:
            descr		+= ite
        for ite in item["com_url"]:
            com_url 	+= ite
        for ite in item["com_scale"]:
            com_scale 	+= ite
        for ite in item["com_prop"]:
            com_prop	+= ite
        for ite in item["com_indust"]:
            com_indust	+= ite
        for ite in item["com_home"]:
            com_home 	+= ite
        for ite in item["com_dress"]:
            com_dress	+= ite
        for ite in item["com_intro"]:
            com_intro	+= ite

        if "-" in mon_pay:
            mon_pay  		= mon_pay.split("-")
            mon_pay_down	= int(mon_pay[0])
            mon_pay_up		= int(mon_pay[1][:-7])
        elif "/" in mon_pay:
            mon_pay_down	= int(mon_pay[:-7])
            mon_pay_up		= mon_pay_down
        if "-" in sub_place:
            sub_place 		= sub_place[1:]
        com_intro 			= com_intro.strip()
        com_dress 			= com_dress.strip()
        com_indust			= com_indust.strip()

        # sql = "insert into company(com_url, com_name, com_scale, com_prop, com_indust, com_home, \
        #     com_dress, com_intro) \
        #     values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') " % \
        #     (com_url, company, com_scale, com_prop, com_indust, com_home, com_dress, com_intro)
        # try:
        #     self.cursor.execute(sql)
        #     self.db.commit()
        #     # raise DropItem("It is ends")
        # except:
        #     self.db.rollback()
        #     # print "it's error on job : %s" % sql

        sql = "select ID from job where url='%s'" % url
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        if not data:
            sql = "insert into job(url, name, company, welfare, mon_pay_down, mon_pay_up, place, sub_place, job_prop, \
                exper, edu, num, classify, descr, com_url, com_scale, com_prop, com_indust, com_home,com_dress, com_intro) \
                values ('%s', '%s', '%s', '%s', '%d', '%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
                (url, name, company, welfare, mon_pay_down, mon_pay_up, place, sub_place, job_prop,
                exper, edu, num, classify, descr, com_url, com_scale, com_prop, com_indust, com_home, com_dress, com_intro)
            try:
                self.cursor.execute(sql)
                self.db.commit()
                #raise DropItem("It is ends")
            except:
                self.db.rollback()
                #print "it's error on job : %s" % sql
        else:
            sql = "update job set date=now() where ID=%d" % data[0]
            # sql = "update into job(url, name, company, welfare, mon_pay_down, mon_pay_up, place, sub_place, job_prop, \
            #     exper, edu, num, classify, descr, com_url, com_scale, com_prop, com_indust, com_home,com_dress, com_intro) \
            #     values ('%s', '%s', '%s', '%s', '%d', '%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
            #     (url, name, company, welfare, mon_pay_down, mon_pay_up, place, sub_place, job_prop,
            #     exper, edu, num, classify, descr, com_url, com_scale, com_prop, com_indust, com_home, com_dress, com_intro)
            try:
                self.cursor.execute(sql)
                self.db.commit()
                print "sueecssful"
                #raise DropItem("It is ends")
            except:
                self.db.rollback()
                #print "it's error on job : %s" % sql
