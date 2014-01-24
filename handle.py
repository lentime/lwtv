#!/usr/bin/python
#coding:utf-8

from data import Tv

def GetList0():#第一个列表
    return Tv.GetName()

def GetList1(value):#第二个列表
    return Tv.GetValue(value).GetName()

def GetList2(value1,value2):#第三个列表
#value1 第一个列表选择的，value2 第二个列表所选择
    return Tv.GetValue(value1).GetValue(value2).GetServeName()

def OpenTv(value1,value2,value3):#打开播放
#value1 第一个列表选择的，value2 第二个列表所选择，value3 第三个列表所选择
    Tv.GetValue(value1).GetValue(value2).OpenWith(value3)
