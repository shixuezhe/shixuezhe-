import scrapy

class CompanySpider(scrapy.Spider):
    name = 'companies'

    @property
    def start_urls(self):
        url_tmp = 'https://www.lagou.com/gongsi/'
        return (url_tmp.format(i) for i in range(1,11))

    def parse(self, response):
        for company in response.css('li.company-item'):
            yield {
                'name':company.xpath('.//p[contains(@class,"company-name")]/a/text()').extract_first(),
                'logo':company.xpath('.//p[contains(@class,"company-name")]/a/@src').extract_first(),
                'type':company.xpath('.//p[contains(@class,"indus-stage")]/text').re(r'\s*(.+)/(.+)/(.+)')[0],
                'finance': company.xpath('.//p[contains(@class,"indus-stage")]/text').re(r'\s*(.+)/(.+)/(.+)')[1],
                'staff_num': company.xpath('.//p[contains(@class,"indus-stage")]/text').re(r'\s*(.+)/(.+)/(.+)')[2],
                'description':company.xpath('.//p[contains(@class,"advantage")]/text').extract_first().strip()
            }
