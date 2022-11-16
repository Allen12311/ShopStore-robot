import time,datetime
from portion import Interval


def TimeSchedule():
    inputtime = datetime.datetime.strptime(input('輸入啟用時間:'),'%H:%M:%S') 
    while True:
        NowTime=datetime.datetime.strptime(time.strftime("%H:%M:%S" ),"%H:%M:%S")
        strNowTime=time.strftime("%Y-%m-%d %H:%M:%S" )
        print('現在時間: ' ,strNowTime ,NowTime > inputtime)#字串型態時間
        # print( NowTime > inputtime)
        time.sleep(1)
        while NowTime > inputtime  :
            print('開始執行排程')
            return
        else : 
            print('排程未開始')


    

