 進入程式路徑 
 git add (上傳檔案)
 git commit -m '增加 README.md' (填寫上傳備註)
 git push 

 virtualenv (套件)

建立虛擬環境
virtualenv (env01) (建立環境名稱)
cd 專案名/環境名/Scripts/
source ./activate (啟動環境)

pip freeze > requirements.txt  (輸出虛擬環境套件)
python -m pip install -r requirements.txt (輸入虛擬套件)


------------------------------------------------------------------------------------------------

 PChome 24h 自動化搶購
安裝套件 email,http,json,select,subprocess,time,datetime, argparse ,tkinter,wsgiref,selenium

參考文件 https://github.com/powei-lin/family_mart_goods_check/blob/main/main.py
安裝exe https://chromedriver.chromium.org/downloads

------------------------------------------------------------------------------------------------

 MoMo 自動化搶購


import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
