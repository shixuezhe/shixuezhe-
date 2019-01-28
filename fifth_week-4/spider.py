#_*_ coding: utf-8 _*_
#ʹ��csv�����ļ�
import csv
#ʹ��asyncio��ʵ���첽
import asyncio
#ʹ��aiohttpʵ����������
import aiohttp
#�����첽�еĳ�ʱ
import async_timeout
#ʹ��scrapy.http�� HtmlResponse����
from scrapy.http import HtmlResponse

results=[]

#�����ȡ��ҳ���ݵ��첽����
async def fetch(session,url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

#������ȡ��ҳ���ݵĺ���
def parse(url,body):
    response =HtmlResponse(url=url,body=body)
    for repository in response.css('li.public'):
        name=repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)')
        update_time=repository.xpath('.//relative-time/@datetime').extract_first()
        results.append((name,update_time))
#�����첽���� 
async def task(url):
    timeout=aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession() as session:
        #����fetch��ȡHTMLҳ��
        html=await fetch(session,url)
        #����parse����ҳ�沢���������results��
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
