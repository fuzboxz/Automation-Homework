import scrapy
from ..items import ImdbscraperItem

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        for url in response.css(".titleColumn a::attr(href)").extract():
            request = scrapy.Request(response.urljoin(url), callback=self.parsePage)
            yield request

    def parsePage(self, response):
        full_cast = response.css(".primary_photo+ td a::text").extract()
        for member in full_cast:
            cast = ImdbscraperItem()
            cast["name"] = str(member).strip()
            yield cast