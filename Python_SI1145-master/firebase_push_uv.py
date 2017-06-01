#!/usr/bin/python -u
# -*- coding: utf-8 -*-
#PyrebaseはPython3で実行する！
#Pyrebaseを使ってfirebaseに値を入れる(PUSH)。
#エラーにより、インストールしたもの(以下４行)：



#import Libraries
import pyrebase
import datetime
import time
import SI1145 as SI1145
import firebaseConfig

#Firebase Configuration
config = firebaseConfig.readConfig()

#initialize app with config
firebase = pyrebase.initialize_app(config)

#Firebase Database Intialization
db = firebase.database()

#SI1145.pyからセンサ(UV, ir, vis)の値を取得する。
sensor = SI1145.SI1145()

#10秒*6回のデータを取得
for num in range(6):
    #現在日時を取得
    now = datetime.datetime.now()
    get_time = now.strftime('%Y/%m/%d %H:%M')

    #UVの値を取得
    UV = sensor.readUV()
    uvIndex = UV / 100.0

    print ("UV: " + str(uvIndex))

    data = {"time": get_time, "UV index": uvIndex}
    #push: save data into Firebase
    db.child("UV index").push(data)
    #10secごと
    time.sleep(10)
