import time,json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import TimeSchedule_API.Time_Scheduler
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
web = webdriver.Chrome(options=options)
with open('momo_pwd.json', 'r') as f:
    jsonFile = json.load(f)
# options.use_chromium = True
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}

options.add_experimental_option('prefs', prefs) 
options.add_argument("disable-infobars") 
web.maximize_window() 


web.get("https://m.momoshop.com.tw/mymomo/login.momo") # 到登入頁面
web.find_element(By.ID, 'memId').send_keys(jsonFile["accton"]) # 輸入帳號
web.find_element(By.ID,'passwd').send_keys(jsonFile["pwd"]) # 輸入密碼 
web.find_element(By.CLASS_NAME, 'login').click()
TimeSchedule_API.Time_Scheduler.TimeSchedule()
# web.get("https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10595871&str_category_code=3801800025&mdiv=3899900000-bt_2_092_01-bt_2_092_01_e16&ctype=B&sourcePageType=4")
web.get('https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=9914113&str_category_code=3801800020&sourcePageType=4')
time.sleep(1)




while 1:
    try:
        startTime=time.time()
        WebDriverWait(web, 10, 0.05).until(EC.presence_of_element_located((By.CLASS_NAME,'buynow'))) # 顯性等待
        time.sleep(1)
        endTime=time.time()
        web.find_element(By.CLASS_NAME,'buynow').click() # 偵測到可以購買按鈕就點擊按鈕 
        web.find_element(By.XPATH,'//*[@id="checkoutBar"]/tbody/tr/td[4]/a').click()
        time.sleep(1)
        web.find_element(By.CLASS_NAME,'confirm').click()
        time.sleep(1)
        web.find_element(By.CLASS_NAME,'recentlyCardNoBtn').click()  
        web.find_element(By.XPATH,'//*[@id="notice705"]/div[2]/div[1]/div[1]/table/tbody/tr/td[1]/label/span').click()
        web.find_element(By.CLASS_NAME,'recentlyCardNoselectBox_confirm').click() 
        web.find_element(By.ID,'cardCVV').send_keys(jsonFile["ccv"])
        web.find_element(By.ID,'orderSave').click()
        print ('已經購買!')
        print('執行時間:%f秒' %(endTime-startTime))
        break 
    except :
        print("還不能購買! 重新整理!")
    web.refresh() # 重整頁面
web.find_element