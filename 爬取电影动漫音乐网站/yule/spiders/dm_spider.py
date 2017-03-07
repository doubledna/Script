#coding=utf8
import scrapy
from yule.items import YuleItem
from scrapy.selector import Selector

class DmSpider(scrapy.Spider):
    name = 'dm'
    allowed_domains = ["dilidili.wang"]
    start_urls = [
        "http://www.dilidili.wang/"
    ]

    def parse(self, response):
        cartons = Selector(response).xpath('//div[@class="clear"]/div/div/div/div/div/ul/li')
        for carton in cartons:
            item = YuleItem()
            item['name'] = carton.xpath(
                'a/p/text()'
            ).extract()
            item['url'] = carton.xpath(
                'a/@href'
            ).extract()
            yield item
