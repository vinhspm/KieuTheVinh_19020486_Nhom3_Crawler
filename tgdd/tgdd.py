import scrapy
import json

class TgddSpider(scrapy.Spider):
    name = 'tgdd'
    allowed_domains = ['thegioididong.com']
    start_urls = ['https://www.thegioididong.com']
#
    def parse(self, response):
        if response.status == 200 and response.css('body section div.rowdetail::attr(id)').get()=='normalproduct':
            data = {
                'link': response.url,
                'tag': [
                    k.strip() for k in response.css('ul.breadcrumb li a::text').getall()
                ], 
                'price': response.css('div.area_price strong::text').get(),
                'img-src': response.css('div.icon-position > img::attr(src)').get(),
                'short-prop' : [
                    q.replace(',','') for q in response.css('ul.parameter li div *::text').getall() 
                ],
            }
            f = open('C:/Users/Vinh/Desktop/thegioigidong/thegioigidong/output/res.txt','a+',encoding='utf8')
            f.write(json.dumps(data, ensure_ascii=False))
            f.write('\n')
        yield from response.follow_all(css='a[href^="https://www.thegioididong.com/"]::attr(href), a[href^="/"]::attr(href)', callback = self.parse)
    