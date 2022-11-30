import json
import select ,subprocess,time,datetime, argparse
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select
import TimeSchedule_API.Time_Scheduler
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# driver_path=ChromeDriverManager(path = r"檔案路徑").install() #下載新版chromedriver，並儲存回指定路徑

URL='https://24h.pchome.com.tw/prod/DDBF0C-A9005132Y'  #商品連結

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("disable-infobars") 
options.page_load_strategy = 'eager'
# options.add_argument("--headless")  # 不開啟實體瀏覽器背景執行

web = webdriver.Chrome(executable_path='chromedriver.exe',options=options)

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


web.get('https://ecvip.pchome.com.tw/login/v3/login.htm?rurl=https%3A%2F%2Fshopping.pchome.com.tw%2F')
web.find_element(By.ID, 'loginAcc').send_keys(jsonFile["accton"]) # 輸入帳號
sleep(1)
web.find_element(By.ID,'loginPwd').send_keys(jsonFile["pwd"]) # 輸入密碼
time.sleep(1)
web.find_element(By.ID, 'btnLogin').click()
time.sleep(2)
TimeSchedule_API.Time_Scheduler.TimeSchedule()

web.get(URL)


while 1:
        try:
            buy = WebDriverWait(web, 1, 00.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ButtonContainer"]/button'))) # 顯性等待
            web.find_element(By.XPATH,'//*[@id="ButtonContainer"]/button').click()
            print ('可以購買!')
            web.get("https://ecssl.pchome.com.tw/sys/cflow/fsindex/BigCar/BIGCAR/ItemList")  #直接前往購物車
            print("前往結帳")

            """
            信用卡 付款
            """
            # print('信用卡結帳')
            # button = web.find_element(By.XPATH, #按下'一次付清'按鈕
            # "//li[@class='CC']/a[@class='ui-btn']")
            # web.execute_script("arguments[0].click();", button)
            """
            信用卡 付款
            """
            
            # sleep(2)
            # web.find_element(By.ID,'BuyerName').send_keys(jsonFile["Name"]) #姓名
            # web.find_element(By.ID,'BuyerSSN').send_keys(jsonFile["SSN"]) #身分證
            # web.find_element(By.ID,'BirthYear').send_keys(jsonFile["BirthYear"]) 
            # web.find_element(By.ID,'BirthMonth').send_keys(jsonFile["BirthMonth"])
            # web.find_element(By.ID,'BirthDay').send_keys(jsonFile["BirthDay"])
            # web.find_element(By.ID,'CardNum_single').send_keys(jsonFile["CardNum_single"]) #卡片號碼
            # multi_ThruMonth =web.find_element(By.ID ,'multi_ThruMonth')
            # ThruMonth=select.Select(multi_ThruMonth) #卡片有效日期月份
            # ThruMonth.select_by_value('01')
            # multi_ThruYear=web.find_element(By.ID ,'multi_ThruYear')
            # ThruYear=select.Select(multi_ThruYear)
            # ThruYear.select_by_value('2027')
            # web.find_element(By.ID,'multi_CVV2Num').send_keys(jsonFile["CCV"]) #驗證碼
            # web.find_element(By.ID,'BuyerMobile').send_keys(jsonFile["Mobile"])  #手機號碼
            # classification =web.find_element(By.ID ,'BuyerAddrCity') #信用卡帳單地址
            # City=select.Select(classification)
            # City.select_by_value('1')
            # BuyerAddrRegion=web.find_element(By.ID,'BuyerAddrRegion')
            # AddrRegion=select.Select(BuyerAddrRegion)
            # AddrRegion.select_by_value('115')
            # web.find_element(By.ID,'BuyerAddr').send_keys(jsonFile["BuyerAddr"]) #詳細地址

            print('貨到付款')
            time.sleep(2)
            web.find_element(By.ID,'a_cod').click() #貨到付款
            time.sleep(2)
            """貨到付款購買資料 """

            web.find_element(By.ID,'BuyerName').send_keys(jsonFile["Name"]) 
            web.find_element(By.ID,'BuyerMobile').send_keys(jsonFile["Mobile"])
            classification =web.find_element(By.ID ,'BuyerAddrCity')
            City=select.Select(classification)
            City.select_by_value('1')
            BuyerAddrRegion=web.find_element(By.ID,'BuyerAddrRegion')
            AddrRegion=select.Select(BuyerAddrRegion)
            AddrRegion.select_by_value('115')
            web.find_element(By.ID,'BuyerAddr').send_keys(jsonFile["BuyerAddr"])


            
            web.find_element(By.ID,'syncData').click()#同步付款資料
            web.find_element(By.XPATH,'//*[@id="frmUserInfo"]/dl[4]/dd[2]/div[1]/div[2]/label/input').click() #選取電子發票類型
            web.find_element(By.ID,'addContact').click() # 按下加入通訊錄(加過可註解)  
            WebDriverWait(web, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='chk_agree']")))  
            web.find_element(By.XPATH,"//input[@name='chk_agree']").click()  # 選取同意按鈕  
            
            
            web.find_element(By.ID,'btnSubmit').click() # 按下確認紐
            print ('可以購買!')

            break 
        except :
            print("還不能購買! 重新整理!")
web.refresh() # 重整頁面
web.find_element


