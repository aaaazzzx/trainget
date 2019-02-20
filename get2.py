import requests
import codecs
import os
from bs4 import BeautifulSoup as bs
import cssselect
from lxml.html import etree
import re

r = requests.get('http://shike.gaotie.cn/lieche.asp?from=%B3%A4%C9%B3&to=%B9%E3%D6%DD')
print(r.encoding)

data = r.text
soup = bs(r.text, 'html.parser')


trainData = soup.find_all('tr', onmouseover='this.className=\'trbgon\'')


#print(soup)
print(len(trainData))
#print(trainData[0])
#print(trainData[1])
cc=[]    # 车次
zm=[]    # 站名
dd=[]    # 到达
kc=[]    # 开车
tl=[]    # 停留
lc=[]    # 里程

for t in trainData:
    # print(t.find('b').string)  # 车次
    aaa = re.search('[A-Z][0-9]{1,}', t.find('b').string , flags=0).group()
    cc.append(aaa)
    try :
        r2 = requests.get('http://shike.gaotie.cn/checi.asp?checi=%s'%(aaa))
        # print(r2.text)
        f = open("%s.html"%(aaa), "w")
        f.write(r2.text)
        print('sucess')
    except IOError:
        print ('Error')
    # f = open("test.htm","w+b")
print(cc)

'''
    data2 = r2.text
    soup2 = bs(r2.text, 'html.parser')
    data22 = soup2.find_all('tr', align='center', bgcolor='#FFFFFF')
    for line in data22:
        zm.append(line.find('a').string)
        td = line.find_all('td')
        #for aaa in td:
        #   print(aaa.string)
        print(td[1].string)
        dd.append(td[1].string)
'''


