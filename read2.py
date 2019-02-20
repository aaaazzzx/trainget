import numpy as np
from read1 import readcc
import matplotlib.pyplot as plt


def shujutongyi(cc):
    data = [] # 数据统一
    for i in range(len(cc)):
        data2 = []     #用于存放该车信息

        c = np.load("%s.npy"%(cc[i]))
        c = c.tolist()

        # print(c)


        data2.append(cc[i])
        data2.append(c)
        # print(data2)
        # data() = cc[i]
        data.append(data2)
    return data

def zmsb(zm):    # 站名识别
    data = ['长沙南站','株洲西站','衡山西站','衡阳东站','耒阳西站','郴州西站','乐昌东站','韶关站','英德西站','清远站','广州北站','广州南站']
    weizhi = data.index(zm)
    zmbh = 11-weizhi
    return zmbh


def xy(data):
    n = len(data)
    # print (n)    # 116,车次总数
    ccxy = []    #
    for i in range(n):
        data2 = data[i]
        # print (data2)
        cc = data2[0]
        # 找出车次位置
        a = data2[1][0].index('长沙南站')
        b = data2[1][0].index('广州南站')
        m = b-a+1    #途径车站数
        # print (a,b,m)
        data4 = []    # '车次+data3+data3'
        data4.append(data2[0])
        for j in range(a,b+1):
            data3 = []  # 站名 + 到达 + 开车
            zmbh = zmsb(data2[1][0][j])
            # print(zmbh)
            dd = data2[1][1][j]
            kc = data2[1][2][j]
            tl = data2[1][3][j]
            lc = data2[1][4][j]
            if tl == '22分钟':
                print(data2[0])
            # print(zmbh, dd, kc, tl, lc)
            data3.append(zmbh)
            data3.append(dd)
            data3.append(kc)
            #print(data3)
            data4.append(data3)
        #print(data4)
        ccxy.append(data4)
    return ccxy




# 不再使用，已完成任务
def zmpx(data):
    px = []
    data2 = []
    for i in range(len(data)):
        data2.append(data[i][1][0])
    # print(data)
    px = data2[0]
    # print(px)
    '''
        for k in range(len(data2)):
            list = data2[k]
            print(list)
            print(data[i][0])
            a = list.index('长沙南站')
            b = list.index('广州南站')
            for j in range(a,b+1):
                list2 = list[j]
                zmbh = zmsb(list2)    # 站名编号
                print(list2,zmbh)
                dd = data[i][1][1][a+j]
                print(dd)
                try:
                    weizhi = px.index(list2)
                except :
                    weizhi = px.index(list[j-1])
                    px.insert(weizhi+1,list2 )



            
            if list2 in px:
                pass
            else:
                px.append(list2)
            
        # print(px)
        '''


    # return px


def ccycl(data5):
    cc = data5[0]
    n = len(data5)
    aaa = []   # y为站名，x为时间
    x = []
    y = []
    for i in range(1,n):
        x.append(data5[i][0])
        if data5[i][1]== '始发站':
            y.append(data5[i][2])
        else:
            y.append(data5[i][1])
        x.append(data5[i][0])
        if data5[i][2]== '终点站':
            y.append(data5[i][1])
        else:
            y.append(data5[i][2])
    #print(x)
    #print(y)
    bbb = [cc,y,x]
    return bbb






def time(x):
    tt = []
    for i in range(len(x)) :
        xx = x[i]
        # print(xx)     # 19:55
        h = int(xx[0:2])
        m = int(xx[3:])
        # print(m)
        t = h*60+m
        # print(t)
        tt.append(t)
    return tt


def main():

    # 读取车次
    cc=readcc()
    # print(cc)

    # 打开对应车次，并操作
    # data = [] # 数据统一
    data = shujutongyi(cc)
    print(data)

    #对车次排序，ok
    # px = zmpx(data)

    # 对每一车次进行数据处理
    ccxy = xy(data)
    print(ccxy)



    fig = plt.figure()  # 创建一个没有 axes 的 figure
    fig.suptitle('CRH IN CS TO GZ')  # 添加标题以便我们辨别
    '''
    y1 = x + 3  # 曲线 y1
    y2 = 3 - x  # 曲线 y2
    plt.figure()  # 定义一个图像窗口
    plt.plot(x, y1)  # 绘制曲线 y1
    plt.plot(x, y2)  # 绘制曲线 y2
    plt.show()
    '''

    # 车次预处理
    for data5 in ccxy:
        [ccc, x, y] = ccycl(data5)     # ccc车次  x 时间 ,y车站
        #print(x)
        tt = time(x)
        #print(tt)
        plt.plot(tt, y)    #绘线
        plt.scatter(tt[1], y[0], s=50)
        plt.text(tt[1], y[0], "%s"%(ccc))  # fontdict设置文本字体
    plt.show()






if __name__ == '__main__':
    main()
