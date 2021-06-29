import json

from selenium import webdriver


def get_cookie():
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.get('https://i.nosec.org/login?service=https://fofa.so/login')

    while True:
        if browser.current_url.startswith('https://fofa.so/'):
            with open('cookies.txt', 'w') as cookief:
                cookief.write(json.dumps(browser.get_cookies()))
            print('cookies保存成功！')
            break
            browser.close()
            browser.quit()

get_cookie()