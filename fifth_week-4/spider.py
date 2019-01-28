#_*_ coding: utf-8 _*_
#使用csv保存文件
import csv
#使用asyncio库实现异步
import asyncio
#使用aiohttp实现网络请求
import aiohttp
#设置异步中的超时
import async_timeout
#使用scrapy.http的 HtmlResponse解析
from scrapy.http import HtmlResponse

results=[]

#定义获取网页内容的异步操作
async def fetch(session,url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

#定义提取网页数据的函数
def parse(url,body):
    response =HtmlResponse(url=url,body=body)
    for repository in response.css('li.public'):
        name=repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)')
        update_time=repository.xpath('.//relative-time/@datetime').extract_first()
        results.append((name,update_time))
#定义异步任务 
async def task(url):
    timeout=aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession() as session:
        #调用fetch获取HTML页面
        html=await fetch(session,url)
        #调用parse解析页面并将结果存入results中
        parse(url,html.encode('utf-8'))
        


def main():
    loop=asyncio.get_event_loop()
    url_template=('https://github.com/shiyanlou?page={}&tab=repositories',
        'https://github.com/shiyanlouafter=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoxOTo1NyswODowMM4FkpYw&tab=repositories',
        'https://github.com/shiyanlouafter=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNVQxMTozMTowNyswODowMM4Bxrsx&tab=repositories',
        'https://github.com/shiyanlouafter=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMFQxMzowMzo1MiswODowMM4BjkvL&tab=repositories'
        )
    tasks=[task(url) for url in url_template]
    loop.run_until_complete(asyncio.gather(*tasks))
    with open('/home/shiyanlou/shiyanlou-repos.csv','w',newline='') as f:
        writer=csv.writer(f)
        writer.writerows(results)

if __name__=='__main__':
    main()
