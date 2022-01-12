# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Covid19WebScraperItem(scrapy.Item):

    Country = scrapy.Field()
    CoronavirusCases = scrapy.Field()
    Deaths = scrapy.Field()
    Recovered = scrapy.Field()