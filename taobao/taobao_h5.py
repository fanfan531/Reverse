# -*- coding: utf-8 -*-
# @Time    : 2020-03-31 10:28
# @Author  : ken
'''

这个脚本只是做了h5模拟请求,没有做模拟登陆拿cookie.

遇到的坑:
1.sign参数顺序一致.
2.需要有登录操作,否则只能请求page=1的数据.
'''
import requests
import json
import time
import execjs
import urllib


class TianMao:
    '''天猫指定店铺爬取'''

    # t = str(int(time.time() * 1000))
    lists = []

    def __init__(self, token,cookie):
        self.token = token
        self.cookie = cookie

    def get_goods_data(self, page):
        '''
        获取分页商品信息
        :param page: 页数
        :return:
        '''
        t = str(int(time.time() * 1000))
        url = None
        '''page=1 url中是str,page!=1 url中是int'''
        if page == 1:
            url = f'https://h5api.m.taobao.com/h5/mtop.taobao.wsearch.appsearch/1.0/?jsv=2.5.1' \
                f'&appKey=12574478' \
                f'&t={t}' \
                f'&sign={self.sign(self.token, page, t)}' \
                '&api=mtop.taobao.wsearch.appSearch' \
                '&v=1.0' \
                '&H5Request=true' \
                '&AntiCreep=true' \
                '&type=jsonp' \
                '&timeout=3000' \
                '&dataType=jsonp' \
                '&callback=mtopjsonp9' \
                f'&data=%7B%22m%22%3A%22shopitemsearch%22%2C%22vm%22%3A%22nw%22%2C%22sversion%22%3A%224.6%22%2C%22shopId%22%3A%22575905230%22%2C%22sellerId%22%3A%222200723654612%22%2C%22style%22%3A%22wf%22%2C%22page%22%3A%22{page}%22%2C%22sort%22%3A%22_coefp%22%2C%22catmap%22%3A%22%22%2C%22wirelessShopCategoryList%22%3A%22%22%7D'
        if page != 1:
            url = f'https://h5api.m.taobao.com/h5/mtop.taobao.wsearch.appsearch/1.0/?jsv=2.5.1' \
                f'&appKey=12574478' \
                f'&t={t}' \
                f'&sign={self.sign(self.token, page, t)}' \
                '&api=mtop.taobao.wsearch.appSearch' \
                '&v=1.0' \
                '&H5Request=true' \
                '&AntiCreep=true' \
                '&type=jsonp' \
                '&timeout=3000' \
                '&dataType=jsonp' \
                '&callback=mtopjsonp9' \
                f'&data=%7B%22m%22%3A%22shopitemsearch%22%2C%22vm%22%3A%22nw%22%2C%22sversion%22%3A%224.6%22%2C%22shopId%22%3A%22575905230%22%2C%22sellerId%22%3A%222200723654612%22%2C%22style%22%3A%22wf%22%2C%22page%22%3A{page}%2C%22sort%22%3A%22_coefp%22%2C%22catmap%22%3A%22%22%2C%22wirelessShopCategoryList%22%3A%22%22%7D'
        print(f'请求URL: {url}')
        headers = {
            'authority': 'h5api.m.taobao.com',
            'method': 'GET',
            'path': url.split('h5api.m.taobao.com')[1],
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'cookie': self.cookie,
            'pragma': 'no-cache',
            'referer': 'https://market.m.taobao.com/app/tb-source-app/shop-auction/pages/auction?_w&sellerId=2200723654612&shopId=575905230&dynamicCard=true&disablePromotionTips=true&shop_navi=allitems&displayShopHeader=true',
            'sec-fetch-dest': 'script',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        }
        result = requests.request('GET', url, headers=headers) # 需要添加代理请求

        cookies = requests.utils.dict_from_cookiejar(result.cookies)
        print(cookies)
        print(f'请求返回数据: {result.text}')

        # 清洗数据
        data = result.text.split('mtopjsonp9(')[1][:-1]
        print(f'清洗后数据: {data}')
        self.clean_data(page, json.loads(data))
        return data

    def sign(self, token, page, t):
        '''参数破解'''
        js = '''    function h(a) {
        function b(a, b) {
            return a << b | a >>> 32 - b
        }
        function c(a, b) {
            var c, d, e, f, g;
            return e = 2147483648 & a,
            f = 2147483648 & b,
            c = 1073741824 & a,
            d = 1073741824 & b,
            g = (1073741823 & a) + (1073741823 & b),
            c & d ? 2147483648 ^ g ^ e ^ f : c | d ? 1073741824 & g ? 3221225472 ^ g ^ e ^ f : 1073741824 ^ g ^ e ^ f : g ^ e ^ f
        }
        function d(a, b, c) {
            return a & b | ~a & c
        }
        function e(a, b, c) {
            return a & c | b & ~c
        }
        function f(a, b, c) {
            return a ^ b ^ c
        }
        function g(a, b, c) {
            return b ^ (a | ~c)
        }
        function h(a, e, f, g, h, i, j) {
            return a = c(a, c(c(d(e, f, g), h), j)),
            c(b(a, i), e)
        }
        function i(a, d, f, g, h, i, j) {
            return a = c(a, c(c(e(d, f, g), h), j)),
            c(b(a, i), d)
        }
        function j(a, d, e, g, h, i, j) {
            return a = c(a, c(c(f(d, e, g), h), j)),
            c(b(a, i), d)
        }
        function k(a, d, e, f, h, i, j) {
            return a = c(a, c(c(g(d, e, f), h), j)),
            c(b(a, i), d)
        }
        function l(a) {
            for (var b, c = a.length, d = c + 8, e = (d - d % 64) / 64, f = 16 * (e + 1), g = new Array(f - 1), h = 0, i = 0; c > i; )
                b = (i - i % 4) / 4,
                h = i % 4 * 8,
                g[b] = g[b] | a.charCodeAt(i) << h,
                i++;
            return b = (i - i % 4) / 4,
            h = i % 4 * 8,
            g[b] = g[b] | 128 << h,
            g[f - 2] = c << 3,
            g[f - 1] = c >>> 29,
            g
        }
        function m(a) {
            var b, c, d = "", e = "";
            for (c = 0; 3 >= c; c++)
                b = a >>> 8 * c & 255,
                e = "0" + b.toString(16),
                d += e.substr(e.length - 2, 2);
            return d
        }
        function n(a) {
            a = a.replace(/\\r\\n/g, "\\n");
            for (var b = "", c = 0; c < a.length; c++) {
                var d = a.charCodeAt(c);
                128 > d ? b += String.fromCharCode(d) : d > 127 && 2048 > d ? (b += String.fromCharCode(d >> 6 | 192),
                b += String.fromCharCode(63 & d | 128)) : (b += String.fromCharCode(d >> 12 | 224),
                b += String.fromCharCode(d >> 6 & 63 | 128),
                b += String.fromCharCode(63 & d | 128))
            }
            return b
        }
        var o, p, q, r, s, t, u, v, w, x = [], y = 7, z = 12, A = 17, B = 22, C = 5, D = 9, E = 14, F = 20, G = 4, H = 11, I = 16, J = 23, K = 6, L = 10, M = 15, N = 21;
        for (a = n(a),
        x = l(a),
        t = 1732584193,
        u = 4023233417,
        v = 2562383102,
        w = 271733878,
        o = 0; o < x.length; o += 16)
            p = t,
            q = u,
            r = v,
            s = w,
            t = h(t, u, v, w, x[o + 0], y, 3614090360),
            w = h(w, t, u, v, x[o + 1], z, 3905402710),
            v = h(v, w, t, u, x[o + 2], A, 606105819),
            u = h(u, v, w, t, x[o + 3], B, 3250441966),
            t = h(t, u, v, w, x[o + 4], y, 4118548399),
            w = h(w, t, u, v, x[o + 5], z, 1200080426),
            v = h(v, w, t, u, x[o + 6], A, 2821735955),
            u = h(u, v, w, t, x[o + 7], B, 4249261313),
            t = h(t, u, v, w, x[o + 8], y, 1770035416),
            w = h(w, t, u, v, x[o + 9], z, 2336552879),
            v = h(v, w, t, u, x[o + 10], A, 4294925233),
            u = h(u, v, w, t, x[o + 11], B, 2304563134),
            t = h(t, u, v, w, x[o + 12], y, 1804603682),
            w = h(w, t, u, v, x[o + 13], z, 4254626195),
            v = h(v, w, t, u, x[o + 14], A, 2792965006),
            u = h(u, v, w, t, x[o + 15], B, 1236535329),
            t = i(t, u, v, w, x[o + 1], C, 4129170786),
            w = i(w, t, u, v, x[o + 6], D, 3225465664),
            v = i(v, w, t, u, x[o + 11], E, 643717713),
            u = i(u, v, w, t, x[o + 0], F, 3921069994),
            t = i(t, u, v, w, x[o + 5], C, 3593408605),
            w = i(w, t, u, v, x[o + 10], D, 38016083),
            v = i(v, w, t, u, x[o + 15], E, 3634488961),
            u = i(u, v, w, t, x[o + 4], F, 3889429448),
            t = i(t, u, v, w, x[o + 9], C, 568446438),
            w = i(w, t, u, v, x[o + 14], D, 3275163606),
            v = i(v, w, t, u, x[o + 3], E, 4107603335),
            u = i(u, v, w, t, x[o + 8], F, 1163531501),
            t = i(t, u, v, w, x[o + 13], C, 2850285829),
            w = i(w, t, u, v, x[o + 2], D, 4243563512),
            v = i(v, w, t, u, x[o + 7], E, 1735328473),
            u = i(u, v, w, t, x[o + 12], F, 2368359562),
            t = j(t, u, v, w, x[o + 5], G, 4294588738),
            w = j(w, t, u, v, x[o + 8], H, 2272392833),
            v = j(v, w, t, u, x[o + 11], I, 1839030562),
            u = j(u, v, w, t, x[o + 14], J, 4259657740),
            t = j(t, u, v, w, x[o + 1], G, 2763975236),
            w = j(w, t, u, v, x[o + 4], H, 1272893353),
            v = j(v, w, t, u, x[o + 7], I, 4139469664),
            u = j(u, v, w, t, x[o + 10], J, 3200236656),
            t = j(t, u, v, w, x[o + 13], G, 681279174),
            w = j(w, t, u, v, x[o + 0], H, 3936430074),
            v = j(v, w, t, u, x[o + 3], I, 3572445317),
            u = j(u, v, w, t, x[o + 6], J, 76029189),
            t = j(t, u, v, w, x[o + 9], G, 3654602809),
            w = j(w, t, u, v, x[o + 12], H, 3873151461),
            v = j(v, w, t, u, x[o + 15], I, 530742520),
            u = j(u, v, w, t, x[o + 2], J, 3299628645),
            t = k(t, u, v, w, x[o + 0], K, 4096336452),
            w = k(w, t, u, v, x[o + 7], L, 1126891415),
            v = k(v, w, t, u, x[o + 14], M, 2878612391),
            u = k(u, v, w, t, x[o + 5], N, 4237533241),
            t = k(t, u, v, w, x[o + 12], K, 1700485571),
            w = k(w, t, u, v, x[o + 3], L, 2399980690),
            v = k(v, w, t, u, x[o + 10], M, 4293915773),
            u = k(u, v, w, t, x[o + 1], N, 2240044497),
            t = k(t, u, v, w, x[o + 8], K, 1873313359),
            w = k(w, t, u, v, x[o + 15], L, 4264355552),
            v = k(v, w, t, u, x[o + 6], M, 2734768916),
            u = k(u, v, w, t, x[o + 13], N, 1309151649),
            t = k(t, u, v, w, x[o + 4], K, 4149444226),
            w = k(w, t, u, v, x[o + 11], L, 3174756917),
            v = k(v, w, t, u, x[o + 2], M, 718787259),
            u = k(u, v, w, t, x[o + 9], N, 3951481745),
            t = c(t, p),
            u = c(u, q),
            v = c(v, r),
            w = c(w, s);
        var O = m(t) + m(u) + m(v) + m(w);
        return O.toLowerCase()
    }'''
        param = None
        if page == 1:
            param = f'{token}&{t}&12574478&' + '{"m":"shopitemsearch","vm":"nw","sversion":"4.6","shopId":"575905230","sellerId":"2200723654612","style":"wf","page":"%s","sort":"_coefp","catmap":"","wirelessShopCategoryList":""}' % page
        if page != 1:
            param = f'{token}&{t}&12574478&' + '{"m":"shopitemsearch","vm":"nw","sversion":"4.6","shopId":"575905230","sellerId":"2200723654612","style":"wf","page":%s,"sort":"_coefp","catmap":"","wirelessShopCategoryList":""}' % page
        ej = execjs.compile(js)
        result = ej.call('h', param)
        logger.info(f'加密参数: {param}')
        logger.info(f'sign值: {result}')
        return result

    def clean_data(self,page, data):
        '''清洗参数'''
        '''
        data : json数据
        '''
        try:
            print(f'第{page}页商品数据: {data["data"]["itemsArray"]}')
            for i in data['data']['itemsArray']:
                data = {
                    'price': i['priceWap'],
                    'sold': i['sold'],
                    'name': i['title']
                }
                TianMao.lists.append(data)
        except BaseException as e:
            pass


if __name__ == '__main__':

    # token需要模拟登录,获取cookie的 _m_h5_tk字段值
    token = '68081ae389bd78cf11da549bd4b7c5d7'
    cookie = ''
    t = TianMao(token,cookie)
    for i in range(1, 11):
        print(f'正在请求第{i}页')
        t.get_goods_data(i)
        time.sleep(3)
    print(f'这次请求所有数据: {TianMao.lists}')


