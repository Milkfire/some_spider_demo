import re
import requests


def getHtml(url):
    r = requests.get(url)
    return r.text


def parsePage(html):
    info = []
    title = re.compile('class="title">(.*?)</a>')
    tit = re.findall(title, html)
    grade = re.compile('pts"><div>(.*?)</div>')
    gra = re.findall(grade, html)
    for i in range(len(tit)):
        info.append([tit[i], gra[i]])
    return info


def printInfo(info, type):
    count = 0
    print('\t{:^3}\t{:^60}\t{:>15}'.format('', '标题', '综合评分'))
    for i in info:
        count += 1
        print("TOP {:<3}\t{:^60}\t{:>10}".format(count, i[0], i[1]))
    print('\n\n\n')


def printType(type):
    if (type == 1):
        print("本日视频排行榜:\n")
    elif (type == 3):
        print("最近三日视频排行榜:\n")
    elif (type == 7):
        print("一周视频排行榜:\n")
    else:
        print("一月视频排行榜:\n")


def main():
    type = [1, 3, 7, 30]
    for i in type:
        url = "https://www.bilibili.com/ranking/all/0/0/" + str(i)
        html = getHtml(url)
        info = parsePage(html)
        printType(i)
        printInfo(info, i)


main()
