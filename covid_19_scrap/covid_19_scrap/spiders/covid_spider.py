import scrapy
from scrapy.linkextractors import LinkExtractor

class CovidSpider(scrapy.Spider):
    name = "covid"

    
    start_urls = [
        'https://www.worldometers.info/coronavirus/#countries'
    ]
    allowed_domains=['https://www.worldometers.info/coronavirus/']
    def __init__(self):
        self.link_extractor = LinkExtractor(allow="https://www.worldometers.info/coronavirus")
    
    def parse(self, response):
        for links in self.link_extractor.extract_links(response):
            with open('covid_links.json', 'a+') as f:
                f.write(f"\n{str(link)}")

            yield response.follow(url=links, callback=self.parse)
            # yield {
            #     'Country': response.css('.label-counter::text')[-1].get().split('\n')[-1],
            #     'TotalCases': response.css('.maincounter-number >span::text')[0].get(),
            #     'TotalDeath': response.css('.maincounter-number >span::text').extract()[1],
            #     'TotalRecovered': response.css('.maincounter-number >span::text').extract()[2]
            # }
    

        # next_page = response.css('a.mt_a::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
