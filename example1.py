# -*- coding: utf-8 -*-
# @Time : 2021/2/5 0005
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example1.py
from mongo_db import client
"""添加一个数据"""
client.test.student.insert_many([{"age": 22, "name": "杨华钟", "sex": "男", "role": "班主任"},
                                 {"age": 23, "name": "长江大学", "sex": "女", "role": ["班主任", "年级主任"]},
                                 {"age": 24, "name": "清华大学", "sex": "男", "role": "班主任大大"},
                                 {"age": 25, "name": "中国人民大学", "sex": "男", "role": "班主任总"}])
