# -*- coding: utf-8 -*-
import Learning.zhenzismsclient as smsclient
import random
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
code = ''
for num in range(1,5):
    code = code + str(random.randint(0, 9))
print(code)
client = smsclient.ZhenziSmsClient('https://sms_developer.zhenzikj.com', 'NmMzZDFmNjFkNjcwNDc1MmZ','asd')
print(client.send('15291837659', '只是Guodong python 测试发的的验证码:'+code))

