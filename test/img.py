# -*- coding: utf-8 -*-
# @Time    : 2020-10-8 10:28
# @Author  : ken

import requests
import json
import re
import os
import time
import openpyxl
import pandas as pd
from bs4 import BeautifulSoup


class Img:

    def __init__(self):
        pass

    def parsing_html(self):
        url = 'https://e-hentai.org/s/b25790d29e/1749720-2'
        proxies = {
            'http': 'http://124.158.168.22:8080',
        }
        headers = {
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
            'Connection': 'close'
        }
        respone = requests.get(url, headers=headers, proxies=proxies)
        print(respone)
        soup = BeautifulSoup(respone.text, 'html.parser')
        url1 = soup.find(id='gdt').find('a').attrs['href']
        print(url1)


    def run_img_download(self, url):
        '''下载图片'''
        url = 'https://qocjqyh.wotmiirdgpmx.hath.network/h/8f9aae6d5d743f854d88e6cbdbcadc1ef4024915-880324-720-15244-jpg/keystamp=1602075000-1803e40eca;fileindex=84583429;xres=org/chapter1_1.jpg'
        respone = requests.get(url)
        with open('/Users/mac/Desktop/ken/test/3.jpg', 'wb') as f:
            f.write(respone.content)
        print('下载完毕.')

    def test(self):
        '''半自动解析'''
        for i in range(1,258+1):
            pass



if __name__ == '__main__':
    i = Img()
    # i.run_img_download('1')
    # i.parsing_html()