#coding: utf-8
#swetch scienceのexampleより引用したもののカスタム版をライブラリとして読み込んで表示する！
# $ python temp_moi_pres.py のコマンドで、"Pressure: " + p + ", Temperature: " + t + ", Humidity: " + h　を表示


#import Libraries
import bme280_custom as bme280 # 作成したライブラリファイルを読み込む
import datetime
import time
import pyrebase
import firebaseConfig


#Firebase Configuration
config = firebaseConfig.readConfig()

#initialize app with config
firebase = pyrebase.initialize_app(config)

#Firebase Database Intialization
db = firebase.database()

#10秒*6回のデータを取得
for num in range(6):
    #現在日時を取得
    now = datetime.datetime.now()
    get_time = now.strftime('%Y/%m/%d %H:%M')

    #bme280_custom.pyからセンサ(温度、湿度、気圧)の値を取得する。
    sensor = bme280.readData()
    t = sensor[0] #temperature
    h = sensor[1] #Humidity
    p = sensor[2] #Pressure

    print ("temp: " + str(t) + " humidity: " + str(h) + " pressure: " + str(p))

    data = {"time": get_time, "temp": t, "humidity": h, "pressure": p}
    #push: save data into Firebase
    db.child("Temp_Hum_Pres").push(data)
    #10secごと
    time.sleep(10)
