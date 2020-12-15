import requests
import poplib
import imaplib
import smtplib
import chardet
import os
import json
import hashlib
import time
from email.mime.text import MIMEText
from email.header import Header
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from loguru import logger


class GetBinanceSupport:
    '''监听币安新币上市'''

    def __init__(self):
        self.md5_values = []

    def getmd5(self, data):
        '''计算文件的md5'''
        m = hashlib.md5()
        # 字符串和文件单独处理
        if isinstance(data, str):
            m.update(data.encode("utf8"))
        else:
            with open(data, 'rb') as f:
                for line in f:
                    m.update(line)
        md5code = m.hexdigest()
        logger.info(f'{data} MD5值: {md5code}')
        return md5code

    def is_md5(self, md5):
        if md5 in self.md5_values:
            return True
        return False

    def get_fxh_binance_announcement(self):
        '''币安上新公告.'''
        headers = {
            'Connection': 'keep-alive',
            'Host': 'api.yshyqxx.com',
            'Origin': 'https://www.binancezh.pro',
            'Referer': 'https://www.binancezh.pro/',
            'lang': 'cn',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        }
        url = 'https://api.yshyqxx.com/gateway-api/v1/public/cms/article/list/query?type=1&pageNo=1&pageSize=5'
        result = requests.get(url=url, verify=False, headers=headers)
        data = json.loads(result.text)
        try:
            for index in range(0, 2):
                for i in data['data']['catalogs'][index]['articles']:
                    if ('创新区上市' in i['title']) or ('充值通道现已开放' in i['title']) or ('新币上线' in i['title']):
                        logger.info(i['title'])
                        md5_value = self.getmd5(i['title'])
                        if not self.is_md5(md5_value):
                            self.sen_email(i['title'])
                            self.md5_values.append(md5_value)
        except BaseException as e:
            logger.exception(f'解析公告json报错: {e}')
        self.md5_values = self.md5_values[:50]
        logger.info(self.md5_values)

    def sen_email1(self, info):
        '''发送提醒邮件'''
        pass

    def sen_email(slfe, subject_name):
        ''''''
        # 发件人和收件人
        sender = '596600794@qq.com'
        receiver = '1204088445@qq.com,596600794@qq.com'

        # 所使用的用来发送邮件的SMTP服务器
        smtpServer = 'smtp.qq.com'

        # 发送邮箱的用户名和授权码（不是登录邮箱的密码）
        username = '596600794@qq.com'
        password = 'sekwdkqmmytjbeah'

        mail_title = subject_name
        mail_body = subject_name

        # 添加对象
        message = MIMEMultipart()
        '''
        发送附件对象;
        使用MIMEMultipart来标示这个邮件是多个部分组成的，然后attach各个部分。如果是附件，则add_header加入附件的声明。
        MIME有很多种类型，这个略麻烦，如果附件是图片格式，我要用MIMEImage，如果是音频，要用MIMEAudio，如果是word、excel，我都不知道该用哪种MIME类型了，得上google去查。
        最懒的方法就是，不管什么类型的附件，都用MIMEApplication，MIMEApplication默认子类型是application/octet-stream。
        '''

        # for file in os.listdir(attachment_path):  # 轮询目录中所有需要发送的附件.
        #     file2 = rf'{attachment_path}\{file}'
        #     att = MIMEApplication(open(file2, 'rb').read())
        #     att.add_header('Content-Disposition', 'attachment', filename=f'{file}')
        #     message.attach(att)  # 加载附件.

        # 发送文本对象
        # strApart = MIMEText(mail_body, 'plain', 'utf-8')  # 邮件正文

        message['From'] = sender  # 邮件上显示的发件人
        message['To'] = str(receiver)  # 邮件上显示的收件人,如果是多人,需要将 list转 string
        message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题

        try:
            smtp = smtplib.SMTP_SSL("smtp.qq.com")
            smtp.connect(smtpServer)
            smtp.login(username, password)  # 登录服务器
            smtp.sendmail(sender, receiver, message.as_string())  # 填入邮件的相关信息并发送
            # smtp = smtplib.SMTP()  # 创建一个连接
            # smtp.connect(smtpServer)  # 连接发送邮件的服务器
            # smtp.login(username, password)  # 登录服务器
            # smtp.sendmail(sender, receiver, message.as_string())  # 填入邮件的相关信息并发送
            logger.info("邮件发送成功！！！")
            smtp.quit()
            return True
        except BaseException as e:
            logger.exception(e)


if __name__ == '__main__':
    gbs = GetBinanceSupport()
    # gbs.sen_email('test忽略')
    while 1:
        try:
            gbs.get_fxh_binance_announcement()
            time.sleep(5*60)
        except Exception as e:
            logger.error(e)
            time.sleep(5*60)