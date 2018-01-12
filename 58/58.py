# coding=utf-8

from lxml import etree
import csv
import time
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'}


def get_data(pn):
    url = 'http://zh.58.com/doumen/chuzu/pn%s/' % pn
    html = requests.get(url, headers=headers).text
    data = etree.HTML(html)
    return data


def get_address(data):
    max_room = len(data.xpath('//ul[@class="listUl"]/li'))
    room_data = []
    for i in range(1, max_room):
        data_list = []
        _data = data.xpath(
            '//ul[@class="listUl"]/li[%s]/div[@class="des"]/h2/a/text()' % i)
        t = _data[0].replace(' ', '').replace('\r\n', '')
        data_list.append(t)
        _data = data.xpath(
            '//ul[@class="listUl"]/li[%s]/div[@class="des"]/p[@class="add"]/a[1]/text()' % i)
        try:
            data_list.append(_data[0])
        except IndexError:
            data_list.append(' ')
        _data = data.xpath(
            '//ul[@class="listUl"]/li[%s]/div[@class="des"]/p[@class="add"]/a[2]/text()' % i)
        try:
            data_list.append(_data[0])
        except IndexError:
            data_list.append(' ')
        _data = data.xpath(
            '//ul[@class="listUl"]/li[%s]/div[@class="des"]/p[@class="room"]/text()' % i)
        r = _data[0].replace(' ', '').replace('\xa0\xa0\xa0\xa0', '|')
        data_list.append(r)
        _data = data.xpath(
            '//ul[@class="listUl"]/li[%s]/div[@class="listliright"]/div[@class="money"]/b/text()' % i)
        try:
            data_list.append(_data[0])
        except:
            data_list.append(' ')
        room_data.append(data_list)
    return room_data


def write_csv(data):
    with open('doumen.csv', 'a') as f:
        datafile = csv.writer(f)
        for d in data:
            print(d)
            datafile.writerow(d)
        print('done')


if __name__ == '__main__':
    for i in range(50):
        data = get_data(i)
        time.sleep(3)
        room_data = get_address(data)
        write_csv(room_data)
