# -*- coding: utf-8 -*-
import scrapy

class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    product_sale_price = scrapy.Field()
    product_category = scrapy.Field()
    product_original_price = scrapy.Field()
    product_availability = scrapy.Field()
    product_sales_rank=scrapy.Field()

class AmazonProductSpider(scrapy.Spider):
    name = "AmazonDeals"
    allowed_domains = ["amazon.com"]

    # Use working product URL below
    start_urls = [
        "https://api.proxycrawl.com/?token=WuEWyhxwW1ceoJ_YG8nyRg&url=https://www.amazon.com/dp/B0046UR4F4",
        "https://api.proxycrawl.com/?token=WuEWyhxwW1ceoJ_YG8nyRg&url=https://www.amazon.com/dp/B00DM9D0ZI"
    ]

    def parse(self, response):
     items = AmazonItem()

     title = response.xpath('//h1[@id="title"]/span/text()').extract()
     sale_price = response.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()
     category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
     availability = response.xpath('//div[@id="availability"]//text()').extract()
     sales_rank = response.xpath('//li[@id="SalesRank"]//text()').extract()
     items['product_name'] = ''.join(title).strip()
     items['product_sale_price'] = ''.join(sale_price).strip()
     items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
     items['product_availability'] = ''.join(availability).strip()
     items['product_sales_rank'] = ''.join(sales_rank).strip()
     yield items

