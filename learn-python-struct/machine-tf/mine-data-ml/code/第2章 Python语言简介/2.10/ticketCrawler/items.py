# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class TicketCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #name
    name = scrapy.Field()
    #time
    time = scrapy.Field()
    #address
    address = scrapy.Field()
    #price
    price = scrapy.Field()
    #type(eg.演唱会)
    type = scrapy.Field()
    #url
    url = scrapy.Field()
    #introduction
    introduction = scrapy.Field()

