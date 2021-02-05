# -*- coding: utf-8 -*-
# @Time : 2021/2/5 0005
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example8.py

import math

from bson import ObjectId

"""查找mongo数据库中的文件"""
from mongo_db import client
from gridfs import GridFS

try:
    db = client.test
    gfs = GridFS(db, collection="music")
    document = gfs.get(ObjectId("601ce0aafadf95a7cb288c6d"))
    file = open("F:\CloudMusic\原点12.mp3", "wb")
    file.write(document.read())
    file.close()

except Exception as e:
    print(e)
