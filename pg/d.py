
#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from lxml import html

cookie = {}

raw_cookies = 'll="108090"; bid=0aLIILdzFwA; gr_user_id=f22e97ca-9696-4565-b88e-3ce07cafb46e; __yadk_uid=nvUHI3T0mcycSqOe6g800qTRYTzx6EnR; viewed="5408882_6321315_1230328_1239791_2298747_1428309_1211041_1055304_1320282_6528928"; _vwo_uuid_v2=0BB6C5ED67CC9C6FB7D4D660124D3BDE|935c32f9b22341d72cb5fe357de499c2; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1510118349%2C%22https%3A%2F%2Fwww.google.com.hk%2F%22%5D; __utmt=1; ps=y; dbcl2="151915513:pIEi0CgJdrE"; ck=FFMp; push_noty_num=0; push_doumail_num=0; __utma=30149280.1465102346.1509072820.1509690339.1510118351.7; __utmb=30149280.6.10.1510118351; __utmc=30149280; __utmz=30149280.1510118351.7.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=30149280.15191; _pk_id.100001.8cb4=ecb03ff1ba9349ae.1509072818.6.1510118901.1509690338.; _pk_ses.100001.8cb4=*'

for line in raw_cookies.split(';'):
    key = line.split("=")[0]
    value = line.split("=")[1]
    cookie[key] = value


page = requests.get('https://www.douban.com/people/rosiel/',cookies=cookie)
print(page.text)

tree = html.fromstring(page.text)


intro_raw = tree.xpath('//span[@id="intro_display"]/text()')


for i in intro_raw:
    intro = i.encode('utf-8')

print(intro)