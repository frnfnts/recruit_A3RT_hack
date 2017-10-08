# coding: utf-8
import scrapy
import re
class PhraseSpider(scrapy.Spider):
    name = 'phrase_spider'
    allowed_domains = ["kakugen.aikotoba.jp"]
    start_urls = ['http://kakugen.aikotoba.jp/kakugen.htm']

    custom_settings = {
        #"DOWNLOAD_DELAY": 0.9,
        "FEED_FORMAT": "csv"
    }
    def __init__(self):
        super(PhraseSpider, self).__init__()

    def parse(self, response):
        pages = response.css("#main section.list2 section a::attr(href)").extract()
        pages = map(response.urljoin, pages)
        for page in pages:
            yield scrapy.Request(page, callback=self.parse_indivisual)


    def parse_indivisual(self, response):
        phrases = response.css('#main p::text').extract()
        phrases = map(lambda x: x.split(u"by")[0], phrases)
        phrases = map(lambda x: x.strip(u" \n・"), phrases)
        phrases = filter(lambda x: x, phrases)

        for phrase in phrases:
            item = MyItem()
            item["phrase"] = phrase
            yield item


class MyItem(scrapy.Item):
    phrase = scrapy.Field()


