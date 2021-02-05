# -*- coding: utf-8 -*-
# @Time : 2021/2/5 0005
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example2.py
"""mongo查询"""
from mongo_db import client
try:
    stu = client.test.student.find({})
    for one in stu:
        print(one["_id"], one["name"])

    print("========================")
    stu = client.test.student.find_one({"name": "长江大学"})
    print(stu["_id"], stu["name"])

except Exception as e:
    print(e)
