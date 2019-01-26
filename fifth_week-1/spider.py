#引入JSON进行序列化
import json
#引入selenium相关内容
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse

#存储爬取的结果
results = []

#使用xpath进行解析数据
def parse(response):
    for comment in response.css('div.comment-list-item'):
        result = dict(
            username=comment.xpath(
                './/a[@class="username"]/text()').extract_first().strip(),
            content=comment.xpath(
                './/div[contains(@class, "comment-item-content")]/p/text()').extract_first()
        )
        print("comment: {}".format(result))
        results.append(result)

#判断是否有下一页，返回true或者false
def has_next_page(response):
    classes = response.xpath(
        '//li[contains(@class, "next-page")]/@class').extract_first()
    return 'disabled' not in classes

#进入下一页
def goto_next_page(driver):
    #获取下一页按钮
    next_page_btn = driver.find_element_by_xpath(
        '//li[contains(@class, "next-page")]')
    #模拟点击操作
    next_page_btn.click()

#等待页面加载完成，当页面页码提取结果和当前页面一样就加载完了
def wait_page_return(driver, page):
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, '//ul[@class="pagination"]/li[@class="active"]'),
            str(page)
        )
    )

#主函数
def spider():
    #创建webdriver，用的是chrome浏览器
    driver = webdriver.Chrome()
    #获取第一个页面
    url = 'https://www.shiyanlou.com/courses/427'
    driver.get(url)
    page = 1
    while True:
        print("crawl page {}".format(page))
        #加载第一页
        wait_page_return(driver, page)
        #获取源代码
        html = driver.page_source
        #构建htmlresponse对象
        response = HtmlResponse(url=url, body=html.encode('utf8'))
        #传回解析数据
        parse(response)
        #如果是最后就停止
        if not has_next_page(response):
            break
        page += 1
        goto_next_page(driver)
    #将结果使用json写入文件
    with open('comments.json', 'w') as f:
        f.write(json.dumps(results))


if __name__ == '__main__':
    spider()
