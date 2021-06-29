import json
from selenium import webdriver
import time
import base64
import sys

q = sys.argv[1]
page = sys.argv[2]
filename = f"urls_{time.strftime('%m%d_%H%M', time.localtime())}.txt"
qbase64 = base64.b64encode(q.encode('utf-8'))
co = webdriver.ChromeOptions()
# co.add_argument('--headless')
co.add_argument('log-level=3')
co.add_experimental_option('excludeSwitches', ['enable-automation'])
#co.add_argument('–disable-gpu')
co.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=co)
browser.implicitly_wait(3)
browser.get('https://fofa.so/')
browser.delete_all_cookies()
with open('cookies.txt', 'r') as cookief:
    cookieslist = json.load(cookief)
    for cookie in cookieslist:
        browser.add_cookie(cookie)

browser.get(f'https://fofa.so/result?qbase64={str(qbase64,"utf-8")}')
for tmp in range(int(page)):
    print(f'第{tmp+1}页')
    while True:
        try:
            time.sleep(3)
            ips = browser.find_elements_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[1]/span[2]/a')
            if ips:
                break
        except Exception:
            print('超时')
            pass
    for i in ips:
        try:
            # is_honeypot = i.find_element_by_xpath('./a[2]').get_attribute('style')
            # is_fraud = i.find_element_by_xpath('./a[3]').get_attribute('style')
            # if 'display:none;' in is_fraud or is_honeypot:
            url = i.get_attribute('href')
            print(url)
            open('result/'+filename, 'a').write(url+'\n')
        except Exception:
            print('error')
    browser.find_element_by_xpath('//i[@class="el-icon el-icon-arrow-right"]').click()
