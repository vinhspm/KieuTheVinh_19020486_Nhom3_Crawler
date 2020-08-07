
import scrapy
import json
OUTPUT_FILENAME = 'C:/Users/Vinh/Desktop/báo/crawler/Output/res.txt'

class DantriSpider(scrapy.Spider):
    name = 'dantri'
    allowed_domains = ['dantri.com.vn']
    start_urls = ['https://dantri.com.vn/']
    
    def parse(self, response):
        if response.status == 200 and response.css('body[class="articlev2  dtv2 "]::attr(data-isrc)').get() == 'articlev2':
            print('crawling')
            data = {
                'link': response.url,
                'title': response.css('h1.dt-news__title::text').get().strip(),
                'description': response.css('div.dt-news__sapo h2::text').get(),
                'author': response.css('div.dt-news__content p > strong::text').get(),
                'tags': [
                    k.strip() for k in response.css('ul.dt-news__tag-list li > h4 a::text').getall()
                        
                ],
                'pub_date':response.css('span.dt-news__time::text').get(),
            }
            f = open(OUTPUT_FILENAME, 'a+', encoding='utf8')
            f.write(json.dumps(data, ensure_ascii=False))
            f.write('\n')
        yield from response.follow_all(css='a[href^="https://dantri.com.vn/"]::attr(href), a[href^="/"]::attr(href)', callback = self.parse)