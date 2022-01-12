import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from ..items import Covid19WebScraperItem

class CovidSpider(scrapy.Spider):
    name = "covid"
    
    start_urls = [
        'https://www.worldometers.info/coronavirus/#countries'
    ]
    allowed_domains=['www.worldometers.info']
   
    def parse(self, response):
        for link in response.css('tbody > tr > td > a.mt_a::attr(href)').getall()[0:224]:
            
            yield response.follow("https://www.worldometers.info/coronavirus/" + link, callback=self.parse_link)
        

    def parse_link(self, response):

        items = Covid19WebScraperItem()

        Country = response.css('.label-counter::text')[-1].get().split('\n')[-1],
        CoronavirusCases = response.css('.maincounter-number >span::text')[0].get(),
        Deaths= response.css('.maincounter-number >span::text').extract()[1],
        Recovered = response.css('.maincounter-number >span::text').extract()[2]
    
        items['Country'] = Country
        items['CoronavirusCases'] = CoronavirusCases
        items['Deaths'] = Deaths 
        items['Recovered'] = Recovered

        yield items  
    
