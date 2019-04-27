import scrapy


#"start_urls" can be altered as per requirements.
class QuotesSpider(scrapy.Spider):
    name = 'news'
    start_urls = [
        'https://www.gadgetsnow.com/latest-news?utm_source=toiweb&utm_medium=referral&utm_campaign=toiweb_hptopnav',
    ]

    def parse(self, response):
        for quote in response.css('li'):
            yield {
                'important': quote.css('span.w_desc::text').get(),   #use .css or .xpath according to simplicity.
                #'very_imp': quote.xpath('span/small/text()').get(),
            }

        

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)