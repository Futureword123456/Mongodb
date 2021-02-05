# -*- coding: utf-8 -*-
# @Time : 2021/2/5 0005
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example5.py
from mongo_db import client
""""分页"""
stu = client.test.student.find({}).skip(0).limit(5)
for one in stu:
    print(one["_id"], one["name"])
print("=========================")
"""去除重复字段值"""
stu = client.test.student.distinct("name")
for one in stu:
    print(one)
print("======================")
"""排序"""
stu = client.test.student.find({}).sort([("name", -1)])
for one in stu:
    print(one["_id"], one["name"])