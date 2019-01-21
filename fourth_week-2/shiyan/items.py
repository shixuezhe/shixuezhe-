# -*- coding: utf-8 -*-
import scrapy


class ShiyanItem(scrapy.Item):
     name = scrapy.Field()
     update_time=scrapy.Field()

