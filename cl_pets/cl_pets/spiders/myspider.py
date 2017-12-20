import scrapy

class MySpider(scrapy.Spider):
    name='cl_pets'
    start_urls=['http://sandiego.craiglist.org/search/pet']
    def parse(self,response):
        for title in response.xpath("//li[@class='result-row']//p"):
            yield{
                "title":title.xpath("a/text()").extract_first()
            }
