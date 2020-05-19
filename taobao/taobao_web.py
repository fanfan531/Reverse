# -*- coding: utf-8 -*-
# @Time    : 2020-03-31 10:28
# @Author  : ken

import requests
import json
import re
import openpyxl
import pandas as pd
from bs4 import BeautifulSoup

class TaobaoWeb:

    def __init__(self, cookie, id, page ):
        '''

        :param cookie:
        :param id: 店铺 id
        '''
        self.cookie = cookie
        self.ids = ids
        self.page = page
        self.pagination=''

    def run_all(self):
        '''爬取店铺全量数据'''
        for id in self.ids:
            for page in range(1, 100):
                if page == 1 or page in self.pagination:
                    self.get_info_all(id, page)


    def get_info_all(self, id, page):
        '''获取店铺信息'''
        if self.cookie == '':return 'cookie为空'
        # 全部宝贝-xhr
        url = 'https://purcotton.tmall.com/i/asynSearch.htm?' \
               '_ksTS=1589276885151_454' \
               '&callback=jsonp455' \
               f'&mid=w-{id}-0' \
               f'&wid={id}' \
               '&path=/search.htm' \
               '&search=y' \
               '&spm=a1z10.3-b-s.w4011-14440378953.454.685282e9Dw8b9v' \
               f'&pageNo={page}' \
               '&tsearch=y'

        path = re.search(r'/i/asynSearch.htm.*', url).group()

        headers = {
            'authority': "purcottonfs.tmall.com",
            'method': "GET",
            # 'path': path,
            'scheme': "https",
            'accept': "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
            'cookie': self.cookie,
            # 'referer': "https://purcottonfs.tmall.com/category-1467700017.htm?spm=a1z10.5-b-s.w4011-21407312848.403.321228a3UqIJky&search=y&catName=%C8%AB%B2%BF%B1%A6%B1%B4&catId=1467700017&pageNo=3",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
            'x-requested-with': "XMLHttpRequest",
        }
        try:
            result = requests.get(url, headers=headers)
            print(result.text)
            self.parsing(result.text)
        except BaseException as e:
            print(e)


    def get_info(self):
        '''获取店铺信息'''

        if self.cookie == '':return 'cookie为空'
        # 全部宝贝-xhr
        url = 'https://purcotton.tmall.com/i/asynSearch.htm?' \
               '_ksTS=1589276885151_454' \
               '&callback=jsonp455' \
               f'&mid=w-{self.id}-0' \
               f'&wid={self.id}' \
               '&path=/search.htm' \
               '&search=y' \
               '&spm=a1z10.3-b-s.w4011-14440378953.454.685282e9Dw8b9v' \
               f'&pageNo={self.page}' \
               '&tsearch=y'

        path = re.search(r'/i/asynSearch.htm.*', url).group()

        headers = {
            'authority': "purcottonfs.tmall.com",
            'method': "GET",
            # 'path': path,
            'scheme': "https",
            'accept': "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
            'cookie': self.cookie,
            # 'referer': "https://purcottonfs.tmall.com/category-1467700017.htm?spm=a1z10.5-b-s.w4011-21407312848.403.321228a3UqIJky&search=y&catName=%C8%AB%B2%BF%B1%A6%B1%B4&catId=1467700017&pageNo=3",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
            'x-requested-with': "XMLHttpRequest",
        }
        try:
            result = requests.get(url, headers=headers)
            print(result.text)
            self.parsing(result.text)
        except BaseException as e:
            print(e)

    def parsing(self,data):
        '''解析返回数据为 json'''
        result = re.search(r'[(].*[)]', data)
        print(result.group()[1:-1])
        html = result.group()[1:-1]
        soup = BeautifulSoup(html, 'html')
        self.pagination = soup.find('div', class_='pagination').text

        item5line1 = soup.find('div', class_='J_TItems').find_all('div', class_='item5line1')
        print(len(item5line1))

        datas = []
        for items in item5line1:
            for item in items.find_all('dl'):
                # print(len(item))
                try:
                    name = item.find('dd', class_='detail').find('a').text.strip()
                    price = item.find('span', class_='c-price').text.strip()
                    sale = item.find('span', class_='sale-num').text.strip()
                    # print(name, price, sale)
                    datas.append([name,price,sale])
                except Exception as e:
                    print(e)
        print(len(datas))
        # df = pd.DataFrame(datas, columns=['名称', '价格', '销量'])
        # print(df)
        # df.to_excel('/Users/mac/Desktop/test.xlsx')


if __name__ == '__main__':
    cookie = "cna=KUZDFSdzdnoCAXFXd0pqSGe4; lid=%E4%BC%97%E7%94%9F%E6%99%AE%E6%B8%A1; enc=hpnbGd4S5OEAKeWu5GJB4hFfqnXIOVGc6%2BhuvxSR%2Bd8DmpO%2FFwP9Jjr8odpxg05n9cNq4qNXscpZDq34k2jrAA%3D%3D; cq=ccp%3D1; sgcookie=D6bGh%2Bib%2FzGxGY3lBFUhs; t=3e1ba2c5af5f6d388b314932cb7cf982; tracknick=%5Cu4F17%5Cu751F%5Cu666E%5Cu6E21; _tb_token_=ee736e6e3376e; cookie2=10c5d52e9c935a83c7f1ea866916f64a; hng=CN%7Czh-CN%7CCNY%7C156; pnm_cku822=; Hm_lvt_dde6ba2851f3db0ddc415ce0f895822e=1589184413,1589275422; Hm_lpvt_dde6ba2851f3db0ddc415ce0f895822e=1589275422; isg=BLW1YX5dB87IvmF1Gb5o49ulxDdvMmlEsn2QMjfacSx7DtUA_4J5FMMIWNI4ToH8; l=eB_TuAtevlsXh-vWBOfwPurza77OSIRAguPzaNbMiTfP_9fp5NQcWZbwhgT9C3GVh6zpR38LqeRQBeYBcS0Rn6WBn7hgPzMmn"
    t = TaobaoWeb(cookie, 14440378953, 1)
    # t.get_info()
    t.parsing(1)