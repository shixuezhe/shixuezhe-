# _*_ coding:utf-8 _*_
import scrapy

class ShiyanlouGithub(scrapy.Spider):

    name='shiyanlou_github'

    start_urls=['https://github.com/shiyanlou?tab=repositories','https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxMCswODowMM4FkpVn&tab=repositories','https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories','https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMVQxODowOTowMiswODowMM4BnQBZ&tab=repositories']
    def parse(self,response):
        for url in response.css('li.public'):
            yield{
                    'name':url.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first('\s*(.+)'),
                    'update_time':url.xpath('.//relative-time/@datetime').extract_first()
                    }
