import json
import select ,subprocess,time,datetime, argparse
from time import sleep
from tkinter import W
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import TimeSchedule_API.Time_Scheduler
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("disable-infobars") 
options.page_load_strategy = 'eager'
web = webdriver.Chrome(options=options)
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs) 
web.maximize_window() 

with open('Pchome_pwd.json', 'r') as f:
    jsonFile = json.load(f)

# options.add_argument('blink-settings=imagesEnabled=false') 




sleep(4)
web.get('https://ecvip.pchome.com.tw/login/v3/login.htm?rurl=https%3A%2F%2Fshopping.pchome.com.tw%2F')
web.find_element(By.ID, 'loginAcc').send_keys(jsonFile["accton"]) # 輸入帳號
sleep(2)
web.find_element(By.ID,'loginPwd').send_keys(jsonFile["pwd"]) # 輸入密碼
web.find_element(By.ID, 'btnLogin').click()
time.sleep(2)
TimeSchedule_API.Time_Scheduler.TimeSchedule()
web.get('https://24h.pchome.com.tw/prod/DRADJ4-A900FMNHK?fq=/S/DRADI7')


while 1:
        try:
            buy = WebDriverWait(web, 1, 00.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ButtonContainer"]/button'))) # 顯性等待
            web.find_element(By.XPATH,'//*[@id="ButtonContainer"]/button').click()
            print ('可以購買!')
            web.get("https://ecssl.pchome.com.tw/sys/cflow/fsindex/BigCar/BIGCAR/ItemList")  #直接前往購物車
            print("前往結帳")

            # web.find_element(By.XPATH,'//*[@id="ButtonContainer"]/button').click()
            time.sleep(0.005)
            web.find_element(By.ID,'a_cod').click()
            time.sleep(0.005)
            web.find_element(By.ID,'btnSubmit').click()
            print ('可以購買!')

            break 
        except :
            print("還不能購買! 重新整理!")
web.refresh() # 重整頁面
web.find_element


