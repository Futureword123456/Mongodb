# -*- coding: utf-8 -*-
# @Time : 2021/2/5 0005
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example3.py

from mongo_db import client

"""修改数据"""
try:
    """把所有的字段加上一个role"""
    client.test.student.update_many({}, {"$set": {"role": ["班主任"]}})
    """把name为长江大学的列sex改为女"""
    client.test.student.update_one({"name": "长江大学"}, {"$set": {"sex": "女"}})
    """在name为北京大学加上role"""
    client.test.student.update_one({"name": "北京大学"}, {"$push": {"role": "年级主任"}})
except Exception as e:
    print(e)
