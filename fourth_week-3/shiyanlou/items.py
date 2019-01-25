# -*- coding: utf-8 -*-


import scrapy


class ShiyanlouItem(scrapy.Item):
    name=scrapy.Field()
    update_time=scrapy.Field()
    commits=scrapy.Field()
    branches=scrapy.Field()
    releases=scrapy.Field()
