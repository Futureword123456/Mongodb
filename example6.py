# -*- coding: utf-8 -*-
# @Time : 2021/2/5 0005
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example6.py

from mongo_db import client
from gridfs import GridFS
""""mongodb 存储GridFS 上传图片、音频、视频到mongo从本地到"""
try:
    db = client.test
    gfs = GridFS(db, collection="music")
    file = open("F:\CloudMusic\原点.mp3", "rb")
    args = {"type": "mp3", "keyword": "原点"}

    gfs.put(file, filename="F:\CloudMusic\原点.mp3", **args)
    file.close()
except Exception as e:
    print(e)
