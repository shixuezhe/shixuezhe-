import scrapy

class CompanySpider(scrapy.Spider):

    name = 'companies'
    def start_urls(self):
        url_tmp = ['https://www.lagou.com/gongsi/']
        return (url_tmp.format(i) for i range(1,11))

    def parse(self, response):
        for company in response.css('li.company-item'):
            yield {
                'name':company.xpath('.//p[@class="company-name wordCut"]/a/text()').extract_first(),
                'logo':company.xpath('.//p[@class="company-name wordCut"]/a/@src').extract_first(),
                'type':company.xpath('.//p[@class="indus-stage wordCut"/text').re(r'(.+)/(.+)/(.+)')[0],
                'finance': company.xpath('.//p[@class="indus-stage wordCut"/text').re(r'(.+)/(.+)/(.+)')[1],
                'staff_num': company.xpath('.//p[@class="indus-stage wordCut"/text').re(r'(.+)/(.+)/(.+)')[2],
                'description':company.xpath('.//p[@class="advantage wordCut"]/text').extract_first().strip()
            }