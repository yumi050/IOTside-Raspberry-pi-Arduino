#!/usr/bin/python -u
# -*- coding: utf-8 -*-
#PyrebaseはPython3で実行する！
#Pyrebaseを使ってfirebaseに照度（LUX）の値を入れる(PUSH)。

#import Libraries
import pyrebase
import datetime
import time
import lux_class
from lux_class import SL_TSL2561
import firebaseConfig


#Firebase Configuration
config = firebaseConfig.readConfig()

#initialize app with config
firebase = pyrebase.initialize_app(config)

#Firebase Database Intialization
db = firebase.database()

#lux_class.pyからセンサの値を取得する。
sensor = SL_TSL2561(0x39,1)
sensor.powerOn
sensor.setIntegrationTime('default')

#10秒*6回のデータを取得
for num in range(6):
    #現在日時を取得
    now = datetime.datetime.now()
    get_time = now.strftime('%Y/%m/%d %H:%M')

    #照度の値を取得
    LUX = sensor.getLux()
    print ("lux: " + str(LUX))

    data = {"time": get_time, "lux": LUX}
    #push: save data into Firebase
    db.child("Lux").push(data)
    #10secごと
    time.sleep(10)
