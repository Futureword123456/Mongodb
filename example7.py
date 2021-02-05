# -*- coding: utf-8 -*-
# @Time : 2021/2/5 0005
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example7.py
import datetime
import math

"""查找mongo数据库中的文件"""
from mongo_db import client
from gridfs import GridFS

try:
    db = client.test
    gfs = GridFS(db, collection="music")
    music = gfs.find_one({"filename": "F:\CloudMusic\原点.mp3"})
    print(music.filename)
    print(music.type)
    print(music.keyword)
    print("%dM" % (math.ceil(music.length / 1024 / 1024)))
    print("---------------------")

    musics = gfs.find({"type": "mp3"})
    for one in musics:
        uploadDate = one.uploadDate + datetime.timedelta(hours=8)
        uploadDate = uploadDate.strftime("%Y-%m-%d %H:%M:%S")
        print(one._id, one.filename, uploadDate)

    print("=============")
except Exception as e:
    print(e)
