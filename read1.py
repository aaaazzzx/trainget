import os
import re
from bs4 import BeautifulSoup as bs
import numpy as np



def readcc():
    try:
        f = open("cc.txt")
        # 将车次规范化
        cc = []
        for eachLiine in f.readlines():  # 读取文件的每一行
            aaa = re.search('[A-Z][0-9]{1,}', eachLiine).group()
            # cc.append(aaa)
            # 此处仅读取高铁和动词车次
            t = re.search(r'G', aaa)
            if t:
                cc.append(aaa)
                # print(aaa)
    except IOError:
        print ('读取车次失败')
    # 去除重复车次
    list = sorted(set(cc), key=cc.index)  # sorted output
    return list


def readhtml(soup):    # 解析html
    # 将返回 站名、到达、开车、停留、里程
    zm = []  # 站名
    dd = []  # 到达
    kc = []  # 开车
    tl = []  # 停留
    lc = []  # 里程

    data = soup.find_all('tr', align='center', bgcolor='#FFFFFF')
    for line in data:
        #print(line)
        #if line.find('strong'):
            #print(line.find('strong').string)
        td = line.find_all('td')
        # for linetd in td:
            # print(linetd.string)
        if td[0].string:    # 排除某些none
            # print(td)
            zm.append(td[1].string)
            dd.append(td[2].string)
            kc.append(td[3].string)
            tl.append(td[4].string)
            lc.append(td[7].string)
    # print(zm,dd,kc,tl,lc)
    cc = [zm,dd,kc,tl,lc]
    # print(cc)
    return  cc    #cc是一个矩阵







def main():
    # 读取车次
    cc=readcc()
    # print(cc)

    # 打开对应车次，并操作
    for c in cc:
        # c 车次
        zm = []  # 站名
        dd = []  # 到达
        kc = []  # 开车
        tl = []  # 停留
        lc = []  # 里程
        html = open('%s.html'%(c),'r',encoding="GB2312")
        soup = bs(html.read(), "html.parser")

        # 读取 站名、到达、开车、停留、里程
        [zm, dd, kc, tl, lc] = readhtml(soup)
        # print(zm, dd, kc, tl, lc)


        # 保存
        bc = np.array([zm, dd, kc, tl, lc])
        # print(bc)
        np.save("%s.npy"%(c), bc)
        c = np.load("%s.npy"%(c))
        print(c)
        # return    #break


if __name__ == '__main__':
    main()
