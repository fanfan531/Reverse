# -*- coding: utf-8 -*-
# @Time    : 2020-03-31 10:28
# @Author  : ken

import requests
import json

class TaobaoWeb:

    def __init__(self):
        pass

    def get_info(self):
        '''获取店铺信息'''
        # 全部宝贝-xhr
        url = 'https://purcottonfs.tmall.com/i/asynSearch.htm?' \
              '_ksTS=1589184972557_670' \
              '&callback=jsonp671' \
              '&mid=w-21407312848-0' \
              '&wid=21407312848' \
              '&path=/category-1467700017.htm' \
              '&spm=a1z10.5-b-s.w4011-21407312848.403.321228a3UqIJky' \
              '&search=y' \
              '&catName=全部宝贝' \
              '&catId=1467700017' \
              '&pageNo=3' \
              '&scid=1467700017'

        headers = {
            'authority': "purcottonfs.tmall.com",
            'method': "GET",
            'path': "/i/asynSearch.htm?_ksTS=1589184972557_670&callback=jsonp671&mid=w-21407312848-0&wid=21407312848&path=/category-1467700017.htm&spm=a1z10.5-b-s.w4011-21407312848.403.321228a3UqIJky&search=y&catName=%C8%AB%B2%BF%B1%A6%B1%B4&catId=1467700017&pageNo=3&scid=1467700017",
            'scheme': "https",
            'accept': "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
            'cookie': "cna=KUZDFSdzdnoCAXFXd0pqSGe4; lid=%E4%BC%97%E7%94%9F%E6%99%AE%E6%B8%A1; enc=hpnbGd4S5OEAKeWu5GJB4hFfqnXIOVGc6%2BhuvxSR%2Bd8DmpO%2FFwP9Jjr8odpxg05n9cNq4qNXscpZDq34k2jrAA%3D%3D; cq=ccp%3D1; sgcookie=D6bGh%2Bib%2FzGxGY3lBFUhs; t=3e1ba2c5af5f6d388b314932cb7cf982; tracknick=%5Cu4F17%5Cu751F%5Cu666E%5Cu6E21; _tb_token_=ee736e6e3376e; cookie2=10c5d52e9c935a83c7f1ea866916f64a; hng=CN%7Czh-CN%7CCNY%7C156; Hm_lvt_dde6ba2851f3db0ddc415ce0f895822e=1589184413; pnm_cku822=; Hm_lpvt_dde6ba2851f3db0ddc415ce0f895822e=1589184482; l=eB_TuAtevlsXhTZXBOfwPurza77OSIRAguPzaNbMiTfP_efp5gXOWZb1kST9C3GVh6zpR38LqeRQBeYBcS0Rn6WBn7hgPzMmn; isg=BNLSiO-S2NQxmyYscq-nSpAEI56049Z9iXwXC5wr_gVwr3KphHMmjdhJHwuT304V",
            'referer': "https://purcottonfs.tmall.com/category-1467700017.htm?spm=a1z10.5-b-s.w4011-21407312848.403.321228a3UqIJky&search=y&catName=%C8%AB%B2%BF%B1%A6%B1%B4&catId=1467700017&pageNo=3",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
            'x-requested-with': "XMLHttpRequest",
        }
        result = requests.get(url, headers=headers)
        print(result.text)







if __name__ == '__main__':
    t = TaobaoWeb()
    t.get_info()