#-*- coding:utf8 -*-
import scrapy
import MySQLdb
from yule.items import YuleItem

class Dy2Spider(scrapy.Spider):
    name = 'dy2'
    allowed_domains = ["quanji.la"]
    start_urls = [
        "http://www.quanji.la/"
    ]

    def parse(self, response):
        for moive in response.xpath('//*[@id="fenlei"]/div/div/ul/li'):
            item = YuleItem()
            item['name'] = moive.xpath(
                'a/text()').extract()
            item['url'] = moive.xpath(
                'a/@href').extract()
            yield item