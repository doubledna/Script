#coding=utf8
import scrapy
import os
import urllib
import MySQLdb
import sys
from yule.items import YuleItem

class DySpider(scrapy.Spider):
    name = 'dy'
    allowed_domains = ["dytt8.net"]
    start_urls = [
        "http://www.dytt8.net/index.html"
    ]

    def parse(self, response):
        for moive in response.xpath('//div[@class = "co_content2"]/ul/a[contains(@href, "/html/gndy")]'):
            item = YuleItem()
            item['name'] = moive.xpath(
                'text()').extract()
            item['url'] = moive.xpath(
                '@href').extract()
            yield item




