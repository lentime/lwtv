#!/usr/bin/python
#coding:utf-8

import subprocess
import shlex
import webbrowser




class TvList():
#储存节目信息列表
    def __init__(self):
        self.Name=None
        self.Url=[]
        self.Open=[]
        self.ServeName=[]
    def Add(self,_Open,_Url,_ServeName,_Freature):
        self.Open.append(_Open)
        self.Url.append(_Url)
        self.ServeName.append(_ServeName+" ["+_Freature+"]")
    def TypeAdd(self,value,value1):
        self.ServeName.append(value.GetServeName())
        self.Open.append(value.GetOpen())
        self.Url.append(value.GetUrl(value1))
    def SetName(self,value):
        self.Name=value
    def GetName(self):
        return self.Name
    def GetServeName(self):
        return self.ServeName
    def GetUrl(self):
        return self.Url
    def GetOpen(self):
        return self.Open
    def OpenWith(self,value):
        if self.Open[value]=="www":
            webbrowser.open_new_tab(self.Url[value])
            return
        subprocess.Popen(shlex.split(self.Open[value]+" "+self.Url[value]))

class ValueList():
#储存节目变量列表
    def __init__(self):
        self.ThisName=None
        self.Name=[]
        self.Value=[]
    def SetThisName(self,_ThisName):   
        self.ThisName=_ThisName
    def GetThisName(self):
        return self.ThisName
    def Add(self,_Value):
        self.Name.append(_Value.GetName())
        self.Value.append(_Value)
    def GetValue(self,Value):
            return self.Value[Value]
    def GetName(self):
            return self.Name

class ListValueList():
#储存列表变量列表
    def __init__(self):
        self.Name=[]
        self.Value=[]
    def Add(self,_Value):
        self.Name.append(_Value.GetThisName())
        self.Value.append(_Value)
    def GetValue(self,Value):
            return self.Value[Value]
    def GetName(self):
            return self.Name

