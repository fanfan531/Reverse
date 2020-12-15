# -*- coding: utf-8 -*-
# @Time    : 2020-03-31 10:28
# @Author  : ken

import requests
import json
import re
import os
import time
import openpyxl
import pandas as pd
from bs4 import BeautifulSoup



def shubao(url):
    # url = 'http://www.shubao2s.net/4_4151/'
    data = requests.get(url)
    # print(data.content.decode('gbk'))
    html = data.content.decode('gbk')
    soup = BeautifulSoup(html, 'html.parser')

    dd_list = soup.find('div', id='list').find_all('dd')
    for i in range(66,len(dd_list)):
        name = dd_list[i].get_text()
        url2 = dd_list[i].find('a').attrs['href']
        url3 = 'http://www.shubao2s.net'+url2
        print(name, url3)
        try:
            keep(name,url3)
            time.sleep(1)
        except:
            print('*'*15, name, url3)
            continue

def keep(name, url3):
    data = requests.get(url3)
    # print(data.content.decode('gbk'))
    try:
        html = data.content.decode('gbk')
    except:
        html = data.content.decode()

    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', id='content')
    # print(content.get_text())
    mkdir = f'/Users/mac/Desktop/荒唐'
    os.makedirs(mkdir,exist_ok=True)
    with open(f'{mkdir}/{name}.txt', 'w')as f:
        for i in content.get_text():
            f.write(i)


def biquge():
    url = 'https://www.biquts.com/menu/23353.html'
    data = requests.get(url)
    html = data.content.decode()
    soup = BeautifulSoup(html, 'html.parser')

    uls = soup.find('div', id='readerlists').find_all('ul')[1]
    for li in uls.find_all('li'):
        url1 = li.find('a').attrs['href']
        z_name = li.find('a').get_text()
        print(z_name, url1)
        url2 = 'https://www.biquts.com'+url1
        keep(z_name,url2)


if __name__ == '__main__':
    # url = 'http://www.shubao2s.net/1_1849/'
    # shubao(url)
    # keep('17', 'http://www.shubao2s.net/4_4151/379049.html')
    biquge()







