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
cc=[]
id=[]

for t in trainData:
    print(t)
    print(t.find('b').string)  # 车次
    cc.append(t.find('b').string)
    print('t的类型是：', type(t))
    tt = t.find('a', class_='resultcSub')
    id.append(tt['onclick'])

print(cc)
print(id)


Data = soup.find(onmouseover='this.className=\'trbgon\'').find('b').string








seid=[]
for line in id:
    aaa=re.search(',[0-9]{1,},', line, flags=0).group()
    seid.append(aaa[1:-1])
print(seid)


with codecs.open('cc.txt', 'w') as f:
    for line in cc:
        f.write(line+'\n')
with codecs.open('id.txt', 'w') as f:
    f.write('\n'.join(seid))