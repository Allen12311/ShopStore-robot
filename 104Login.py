import json,time,datetime,os
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_cookies(browser):
    '''Get Cookies and save file'''
    dictCookies = browser.get_cookies()
    jsonCookies = json.dumps(dictCookies,indent=4,ensure_ascii=False)
    with open('cookies.json','w') as f:
        f.write(jsonCookies)

if __name__ == "__main__":
    acount, pwd = input('input Account :'), input('input Pwd :')
    url = 'https://pro.104.com.tw/psc2'
    webDriver = webdriver.Chrome(executable_path='chromedriver.exe')
    webDriver.implicitly_wait(120)
    webDriver.get(url)
    webDriver.maximize_window()
    accounttext = webDriver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[1]/div[2]/input')
    pwdtext = webDriver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[2]/div[2]/input')
    loginbtn = webDriver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[3]/button')

    #如果沒有 cookies.json 檔就先手動登入並輸入驗證碼後產生 cookies.json 檔
    if not os.path.isfile('cookies.json') :
        accounttext.send_keys(acount)
        pwdtext.send_keys(pwd)
        loginbtn.click()
        time.sleep(90)
        get_cookies(webDriver)
        os._exit(0)

    # Add Cookies to webDriver
    with open(r'cookies.json','r') as f:
        cookies = json.load(f)
    for cookie in cookies:
        webDriver.add_cookie(cookie)

    #帶 cookies 登入
    accounttext.send_keys(acount)
    pwdtext.send_keys(pwd)
    loginbtn.click()
    time1 = datetime.datetime.strptime('08:30:00', '%H:%M:%S') #打開卡使時間
    time2 = datetime.datetime.strptime('09:30:00', '%H:%M:%S') #遲到時間
    while True :
        nowtime = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'), '%H:%M:%S') #現在時間
        if nowtime >= time1 and nowtime <= time2:
            webDriver.find_element(By.CLASS_NAME,'btn-block').click() #點擊打卡
        time.sleep(60*5) #五分鐘檢查一次
