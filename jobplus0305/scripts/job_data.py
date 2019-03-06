import scrapy

class JobSpider(scrapy.Spider):

    name = 'jobs'
    def start_urls(self):
        url_tmp = ['https://www.lagou.com/zhaopin/']
        return (url_tmp.format(i) for i range(1,11))

    def parse(self, response):
        for job in response.css('div.con_list_item'):
            yield {
                'name':job.xpath('.//h2[@class="list_item_top"]/h3/text()').extract_first().strip(),
                'location':job.xpath('.//span[@class="add"]/em/text()').extract_first().strip(),
                'experience':job.xpath('.//div[@class="p_bot"]/div/text').re(r'\s*(.+) /\ (.+)\s*'')[0]
                'degree':job.xpath('.//div[@class="p_bot"]/div/text').re(r'\s*(.+) /\ (.+)\s*'')[1]
                'wage_low':job.xpath('.//span[@class="money"]/text()').re(r'(.+)-(.+)')[0]
                'wage_high': job.xpath('.//span[@class="money"]/text()').re(r'(.+)-(.+)')[1]
                'tags':job.xpath('.//div[@class="list_item_bot"]'/span/text()').exreact()
                }


