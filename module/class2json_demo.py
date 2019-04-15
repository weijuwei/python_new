#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(stu):
    return {
        'name': stu.name,
        'age': stu.age,
        'score': stu.score
    }

s = Student('Bob',20,97)

sj = json.dumps(s,default=student2dict)

print(sj)
