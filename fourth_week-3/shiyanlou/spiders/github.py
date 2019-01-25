# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    @property
    def start_urls(self):
        return('https://github.com/shiyanlou?tab=repositories',)
    def parse(self, response):
        for course in response.css('li.public'):
            item=ShiyanlouItem()
            item['name']=course.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)')
            item['update_time']=course.xpath('.//relative-time/@datetime').extract_first()
            course_url=response.urljoin(course.xpath('.//a/@href').extract_first())
            request=scrapy.Request(course_url,callback=self.parse_content)
            request.meta['item']=item
            yield request
        spans = response.css('div.pagination span.disabled::text')
        if len(spans) == 0 or spans[-1].extract() != 'Next':
            next_url=response.css('div.pagination a:last-child::attr(href)').extract_first()
            yield response.follow(next_url,callback=self.parse)
    def parse_content(self,response):
        item=response.meta['item']
        for number in response.css('ul.numbers-summary li'):
            type_text = number.xpath('.//a/text()').re_first(r'\n\s*(.*)\n')
            number_text = number.xpath('.//span[@class="num text-emphasized"]/text()').re_first(r'\n\s*(.*)\n')
            if type_text and number_text:
                number_text = number_text.replace(',', '')
                if type_text in ('commit', 'commits'):
                    item['commits'] = int(number_text)
                elif type_text in ('branch', 'branches'):
                    item['branches'] = int(number_text)
                elif type_text in ('release', 'releases'):
                    item['releases'] = int(number_text)
        yield item

