# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
import json
import csv
import os
import time


def jobs_for_city(city, key, page):
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Host": "www.lagou.com",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://www.lagou.com",
        "Referer": "https://www.lagou.com/jobs/list_%s?px=default&city=%s" % (key.lower(), city),
        "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    }
    post_data = {
        'first': 'true',
        'pn': '%s' % page,
        'kd': '%s' % key.title(),
    }
    url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%s&needAddtionalResult=false&isSchoolJob=0" % city
    json_data = requests.post(url, headers=headers, data=post_data).text
    data = json.loads(json_data)
    position_results = []
    if data['success'] == True:
        positions = data['content']['positionResult']['result']
        for item in positions:
            positionName = item['positionName']
            companshortyname = item['companyShortName']
            conmpanyfullname = item['companyFullName']
            companySize = item['companySize']
            district = item['district']
            education = item['education']
            salary = item['salary']
            workYear = item['workYear']
            positionAdvantage = item['positionAdvantage']
            results = positionName, companshortyname, conmpanyfullname, companySize, district, education, salary, workYear, positionAdvantage
            position_results.append(results)
    return position_results


def write_csv(city, key, page):
    with open(key + '.csv', 'w') as f:
        datafile = csv.writer(f)
        for p in range(1, page + 1):
            jobs = jobs_for_city(city, key, p)
            for job in jobs:
                datafile.writerow(job)
            print('第%s页获取成功' % p)
            time.sleep(2)

if __name__ == '__main__':
    city = raw_input(u'请输入城市>>>')
    key = raw_input(u'请输入职位>>>')
    page = int(raw_input(u'请输入页码>>>'))
    write_csv(city, key, page)
