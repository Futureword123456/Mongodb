# -*- coding: utf-8 -*-
# @Time : 2021/2/5 0005
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example4.py

from mongo_db import client

"""删除一条数据"""
try:
    # client.test.student.delete_one({"name": "北京大学"})
    client.test.student.delete_many({})
    print("删除成功")
except Exception as e:
    print(e)