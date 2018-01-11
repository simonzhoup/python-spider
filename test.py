# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from lxml import etree
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('lang=zh_CN.UTF-8')
# chrome_options.add_argument(
#     'user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
chrome_options.add_argument(
    '"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"')
# chrome_options.add_argument(
#     "'Cookie': 'uuid=32ee726f264a46708b1b.1515629684.1.0.0; mtcdn=K; _lxsdk_cuid=160e2933bfabe-0e78cb1691f06-3a75045d-15f900-160e2933bfbc8; _lxsdk=160e2933bfabe-0e78cb1691f06-3a75045d-15f900-160e2933bfbc8; __mta=154926599.1515629789054.1515629789054.1515629789054.1; ci=108; w_uuid=E4EbWq7v2RJyZE_6Fk7PR5uN_R-zoDKQTUhC9T-RyNo78xbs3Ztbsk0asgC7qaZP; w_visitid=00edbc00-8b78-4961-b6bc-9697fd635d0d; w_cid=0; waddrname=; w_geoid=webw6k1nf0k6; w_ah=; JSESSIONID=1xpmad9ycwtpttl4md9qh4mx7'")
# chrome_options.add_argument(
#     "'Host': 'waimai.meituan.com'")
# chrome_options.add_argument(
#     "'Referer': 'http://waimai.meituan.com/home/webw6k1nf0k6'")
# chrome_options.add_argument(
#     "'Accept': '*/*'")
# chrome_options.add_argument(
#     '"Accept-Encoding": "gzip, deflate"')
# chrome_options.add_argument(
#     '"Accept-Language": "zh-CN,zh;q=0.9"')
# chrome_options.add_argument(
#     "'Connection': 'keep-alive'")
# chrome_options.add_argument(
#     '"X-Requested-With": "XMLHttpRequest"')


browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get(
    u'http://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3021371422&pf_rd_r=17SPWVAT4JHAFH31G4XG&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_ql_3')
sleep(3)
content = browser.page_source.encode('utf-8')
print(content)
data = etree.HTML(content)
# name = data.xpath(u'//div[@class="poilist"]/div/a/@href')
# print(name)
browser.quit()
