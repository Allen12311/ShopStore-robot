import json,time,datetime,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# driver_path=ChromeDriverManager(path = r"檔案路徑").install() #下載新版chromedriver，並儲存回指定路徑
# driver = webdriver.Chrome(service=Service(driver_path)) 

if __name__ == "__main__":
    filePath = 'pwd.json'
    with open(filePath,'r') as f :
        condata = json.load(f)
    acount, pwd, status =condata['acount'], condata['pwd'], 0
    url = 'https://pro.104.com.tw/psc2'
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") 
    options.add_experimental_option('useAutomationExtension', False)
    webDriver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
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
        time.sleep(40)
        print('寫入json')
        with open('cookies.json','w') as f:
            f.write(json.dumps(webDriver.get_cookies(),indent=4,ensure_ascii=False))
        os._exit(0)

    # Add Cookies to webDriver
    with open('cookies.json','r') as f:
        for cookie in json.load(f):
            webDriver.add_cookie(cookie)
    print('登入成功')
    #帶 cookies 登入
    accounttext.send_keys(acount)
    pwdtext.send_keys(pwd)
    loginbtn.click()
    time1 = datetime.datetime.strptime('08:30:00', '%H:%M:%S') #打開卡使時間
    time2 = datetime.datetime.strptime('09:30:00', '%H:%M:%S') #遲到時間
    time3 = datetime.datetime.strptime('17:30:00', '%H:%M:%S') #打開卡使時間
    time4 = datetime.datetime.strptime('18:30:00', '%H:%M:%S') #關閉時間
    while True :
        nowtime = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'), '%H:%M:%S') #現在時間
        if status !=1 and nowtime >= time1 and nowtime <= time2 :
            # webDriver.find_element(By.CLASS_NAME,'btn-block').click() #點擊打卡
            print('開始上班打卡')
            status = 1
            condata['Punchin'] = nowtime.strftime('%H:%M:%S')
            with open(filePath,'w') as f :
                f.write(json.dumps(condata,indent=4,ensure_ascii=False))
        if status != 2 and nowtime >= time3 and nowtime <= time4 :
            if not condata['Punchin'] or nowtime > datetime.datetime.strptime(condata['Punchin'],'%H:%M:%S')+datetime.timedelta(hours=9) :
                webDriver.find_element(By.CLASS_NAME,'btn-block').click() #點擊打卡
                print('開始下班打卡')
                status = 2
        time.sleep(60*5) #五分鐘檢查一次
