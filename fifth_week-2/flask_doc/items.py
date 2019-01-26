# -*- coding: utf-8 -*-

import scrapy

class PageItem(scrapy.Item):
    url = scrapy.Field()
    text=scrapy.Field()
    
