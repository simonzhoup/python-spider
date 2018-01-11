# coding=utf-8

from lxml import etree
import csv
import time
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'}


def get_title_and_mold(data):
    title_list = data.xpath(
        '//ul[@class="listUl"]/li/div[@class="des"]/h2/a/text()')
    # 清洗数据
    molds = []
    titles = []
    for t in title_list:
        t = t.replace(' ', '').replace('\r\n', '')
        mold, title = t.split('|')[0], t.split('|')[1]
        molds.append(mold)
        titles.append(title)
    return molds, titles


def get_data():
    url = 'http://zh.58.com/doumen/chuzu/'
    html = requests.get(url, headers=headers).text
    data = etree.HTML(html)
    return data


def get_room_data(data):
    rooms_list = data.xpath(
        '//ul[@class="listUl"]/li/div[@class="des"]/p[@class="room"]/text()')
    loyouts = []
    areas = []
    for r in rooms_list:
        r = r.replace(' ', '').replace('\xa0\xa0\xa0\xa0', '|')
        loyouts.append(r.split('|')[0])
        areas.append(r.split('|')[1])
    return loyouts, areas


def get_address(data):
	max_room = len(data.xpath('//ul[@class="listUl"]/li/@sortid'))
    addres = []
	for i in range(1,max_room)
	    address1 = data.xpath(
	        '//ul[@class="listUl"]/li[%s]/div[@class="des"]/p[@class="add"]/a[1]/text()' %i)
	    address2 = data.xpath(
	        '//ul[@class="listUl"]/li[%s]/div[@class="des"]/p[@class="add"]/a[2]/text()' %i)
        addres.append(address1[x] + address2[x])
    return addres

data = get_data()

print(get_address(data))
