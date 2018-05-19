# -*- coding: utf-8 -*-
import scrapy


class EbaySpider(scrapy.Spider):
    name = "eBay"
    start_urls = (
        'https://www.ebay.com/rpp/computers-networking/Laptops-Under-399',
    )

    custom_settings = {
    	'FEED_URI':'tmp/eBay.csv'

    }

    def parse(self, response):
		titles= response.css("div.slashui-image-cntr img::attr(alt)").extract()
		prices = response.css('span[itemprop="price"]::text').extract()
		image_urls = response.css("div.slashui-image-cntr img::attr(src)").extract()
		for item in zip(titles,prices,image_urls):
			yield{
				"name" : item[0],
				"price" : item[1],
				"image_urls" : [item[2],],
			}

        
