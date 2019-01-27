# -*- coding: utf-8 -*-

import scrapy


class MovieItem(scrapy.Item):
    url=scrapy.Field()
    name=scrapy.Field()
    summary=scrapy.Field()
    score=scrapy.Field()
