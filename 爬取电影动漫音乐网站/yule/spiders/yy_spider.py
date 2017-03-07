#coding=utf8
import scrapy
from yule.items import YuleItem
from scrapy.selector import Selector

class YySpider(scrapy.Spider):
    name = 'yy'
    allowed_domains = ["9ku.com"]
    start_urls = [
        "http://www.9ku.com/zhuanji/83.htm"
    ]

    def parse(self, response):
        musics = Selector(response).xpath('//*[@id="fall"]/div/*[@id]/li')
        for music in musics:
            item = YuleItem()
            item['name'] = music.xpath(
                'a[@class = "songName"]/text()'
            ).extract()
            item['url'] = music.xpath(
                'a[@class = "songName"]/@href'
            ).extract()
            yield item
