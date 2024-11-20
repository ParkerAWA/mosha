# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 爬虫获取的数据需要封装成Item对象，Item对象中封装了爬取到的数据

class MovieItem(scrapy.Item):
    title = scrapy.Field()
    rank = scrapy.Field()
    subject = scrapy.Field()
    time = scrapy.Field()
    director = scrapy.Field()
