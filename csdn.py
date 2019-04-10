#coding = utf-8
import datetime
import decimal
import re
import time

import sys
import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup as bs


# 访问我的博客
def spider(url, headers):
    r = requests.get(url=url, headers=headers)
    html = r.text
    # 解析html代码
    soup = bs(html, 'lxml')
    #ul = soup.find(name='div', attrs={'class': 'grade-box'})
    # 获取ul下的第一个li节点,正则表达式需要字符串，所以转化一下
    #li = str(ul("dl")[3])
    numbers =re.findall(r'title="(.+?)">\n<dt>排名：', str(soup))
    # print(numbers)
    # 获取当前年月日
    date = time.strftime("%Y-%m-%d", time.localtime())
    # 拼接日期
    numbers.append(date)
    text_save(numbers, 'visitorNumber.txt')
    print('成功执行!',numbers)
 
# 文件存储
def text_save(content, filename, mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename, mode)
    for i in range(len(content)):
        # 如果索引为最后一位，去掉空格且拼上换行符，否则剩下的后面拼接逗号
        if i == len(content) - 1:
            number = (content[i]) + '\n'
        else:
            number = str(content[i]) + ','
        file.write(number)
    file.close()
 
#根据数据动态画图
def drawBydata():
    #读取输出的txt文档
    (recordDate,y) = readData('visitorNumber.txt')
    #获取记录的日期列表范围(0,)
    x = range(len(recordDate))
    # plt.figure() 开始画图,r:红色 
    plt.plot(x,y,'ro-')
    #rotation,x轴字体旋转的角度
    plt.xticks(x, recordDate,rotation=70)
    plt.margins(0.08)
    plt.subplots_adjust(bottom=0.15)
    #设置x轴的名字
    plt.xlabel("Date")
    plt.ylabel("Visitors")
    #图的标题
    plt.title("My blog visit analysis") 
    plt.show()
    print('执行成功！') 

#读取数据
def readData(fileName):
    #以只读文件打开
    inFile = open(fileName,'r')
    #定义第一列数据为博客访问量
    visitors = []
    #第二列数据为日期
    recordDate = []
    #遍历文件每一行
    for line in inFile:
        #逗号分隔
        trainingSet = line.split(',')
        #将第一列和第二列数据拼入对应的列表中
        visitors.append(trainingSet[0])
        recordDate.append(trainingSet[1])
    inFile.close()
    return (recordDate,visitors)

 
if __name__ == '__main__':
 
    url = "https://blog.csdn.net/admans"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'blog.csdn.net',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    spider(url, headers)
    drawBydata()
    print(sys.path)
