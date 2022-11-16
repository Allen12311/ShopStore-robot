from email import header
from http import cookies
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
options.add_experimental_option('excludeSwitches', ['enable-logging'])
web = webdriver.Chrome(options=options)
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}

options.add_experimental_option('prefs', prefs) 
options.add_argument("disable-infobars") 
web.maximize_window() 


sleep(4)
web.get('https://ecvip.pchome.com.tw/login/v3/login.htm?rurl=https%3A%2F%2Fshopping.pchome.com.tw%2F')
web.find_element(By.ID, 'loginAcc').send_keys('allen.zhou@pixis.com.tw') # 輸入帳號
sleep(2)
web.find_element(By.ID,'loginPwd').send_keys('123456') # 輸入密碼
sleep(2)
web.find_element(By.ID, 'btnLogin').click()
TimeSchedule_API.Time_Scheduler.TimeSchedule()

web.get('https://24h.pchome.com.tw/prod/DRADJ4-A900FMNHK?fq=/S/DRADI7')


while 1:
        try:
            buy = WebDriverWait(web, 1, 00.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'//*[@id="ButtonContainer"]/button'))) # 顯性等待
        # web.find_element(By.CLASS_NAME,'buynow').click() # 偵測到可以購買按鈕就點擊按鈕 
            print ('可以購買!')
            web.find_element(By.XPATH,'//*[@id="ButtonContainer"]/button').click()
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


