import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor

class CovidSpider(scrapy.Spider):
    name = "covid"

    
    start_urls = [
        'https://www.worldometers.info/coronavirus/#countries'
    ]
    allowed_domains=['www.worldometers.info']
   
    def parse(self, response):
        for links in response.css('tbody > tr > td > a.mt_a::attr(href)'):
            #newLink = "https://www.worldometers.info/coronavirus/" + links.get()
            # yield{
            #     'link' : newLink
            # }
            yield response.follow("https://www.worldometers.info/coronavirus/" + links.get(), callback=self.parse_link)
            # with open('covid_links.json', 'a+') as f:
            #     f.write(f"\n{str(links)}")

        #     links = response.follow(url=links, callback=self.parse)
        # print(links[27:250])

    def parse_link(self, response):

             yield {
                 'Country': response.css('.label-counter::text')[-1].get().split('\n')[-1],
                  'TotalCases': response.css('.maincounter-number >span::text')[0].get(),
                  'TotalDeath': response.css('.maincounter-number >span::text').extract()[1],
                  'TotalRecovered': response.css('.maincounter-number >span::text').extract()[2]
              }
    

        # next_page = response.css('a.mt_a::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
