import scrapy
import json


class FptSpider(scrapy.Spider):
    name = 'fpt'
    allowed_domains = ['fptplay.vn']
    start_urls = ['https://fptplay.vn/']

    def parse(self, response):
        if response.status == 200 and  '/chi-tiet-video/' in response.url:
            data = {
                'link': response.url,
                'title': response.css('div.film-title h4::text').get(),
                'description': response.css('div.film-desc *::text').get(),
                'director' : response.css('table tr td a[data-scp = "Đạo diễn"]::attr(data-ctn)').get(),
                'actor' : [
                    k.strip() for k in response.css('table tr td a[data-scp = "Diễn viên"]::attr(data-ctn)').getall()
                ],
            }
            f = open('C:/Users/Vinh/Desktop/fptplay/fptplay/output/res.txt', 'a+', encoding='utf8')
            f.write(json.dumps(data, ensure_ascii=False))
            f.write('\n')
        yield from response.follow_all(css='a[href^="https://fptplay.vn/"]::attr(href), a[href^="/"]::attr(href)', callback = self.parse)


