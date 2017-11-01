# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from stack.items import StackItem


class StackCrawlerSpider(CrawlSpider):
    name = 'stack_crawler'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['http://stackoverflow.com/questions?pagesize=50&sort=newest']

    rules = (
        Rule(LinkExtractor(allow=r'questions?page=[0-9]&sort=newest'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        questions = response.xpath('//dib[@class="summary"]/h3')

        for question in questions:
            item = StackItem()
            itme['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
            item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
            yield item
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

