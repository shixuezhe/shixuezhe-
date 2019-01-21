# -*- coding: utf-8 -*-
import scrapy
from shiyan.items import ShiyanItem

class TestSpider(scrapy.Spider):
    name = 'test'
    @property
    def start_urls(self):
        url_tmp1=['https://github.com/shiyanlou?tab=repositories',
                   'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxMCswODowMM4FkpVn&tab=repositories',
                   'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories',
                   'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMVQxODowOTowMiswODowMM4BnQBZ&tab=repositories']
        return url_tmp1
    def parse(self, response):
        for user in response.css('li.public'):
            item=ShiyanItem({
                'name':user.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first('\s*(.+)'),
                'update_time':user.xpath('.//relative-time/@datetime').extract_first()
                })
            yield item
