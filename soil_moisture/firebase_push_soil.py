#!/usr/bin/python
# -*- coding: utf-8 -*-
#PyrebaseはPython3で実行する！
#Pyrebaseを使ってfirebaseに土壌水分の値を入れる(PUSH)。


#import Libraries
import pyrebase
import datetime
import time
import smbus
import firebaseConfig

#Firebase Configuration
config = firebaseConfig.readConfig()

#initialize app with config
firebase = pyrebase.initialize_app(config)

#Firebase Database Intialization
db = firebase.database()

#smbus
i2c = smbus.SMBus(1) #I2Cには０と１があって、１を使用すること！

#10秒*6回のデータを取得
for num in range(6):
    #現在日時を取得
    now = datetime.datetime.now()
    get_time = now.strftime('%Y/%m/%d %H:%M')

    #照度の値を取得
    soil = i2c.read_byte_data(0x10,0) #土壌センサのアドレス番号：0x10
    print ("土壌水分 : " + str(soil))

    data = {"time": get_time, "soil_moisture": soil}
    #push: save data into Firebase
    db.child("soil_moisture").push(data)
    #10秒ごと
    time.sleep(10)
