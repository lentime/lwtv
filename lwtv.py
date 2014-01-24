#!/usr/bin/python
#coding:utf-8
#dshdio@163.com
#2013-1-24

from handle import GetList0
from handle import GetList1
from handle import GetList2
from handle import OpenTv



list0=GetList0()
import wx

def Setlist(evt):
    TvList=GetList1(wx.ListBox.GetSelection(listbox0))
    wx.ListBox.Clear(listbox1)
    wx.ListBox.Clear(listbox2)
    if TvList==None:
        return
    wx.ListBox.InsertItems(listbox1,TvList,0)

def SetBlist(evt):
    TvList=GetList2(wx.ListBox.GetSelection(listbox0),wx.ListBox.GetSelection(listbox1))
    wx.ListBox.Clear(listbox2)
    if TvList==None:
        return
    wx.ListBox.InsertItems(listbox2,TvList,0)
def Open(evt):
    OpenTv(wx.ListBox.GetSelection(listbox0),wx.ListBox.GetSelection(listbox1),wx.ListBox.GetSelection(listbox2))

app = wx.App()
gui=wx.Frame(None)
wx.Frame.SetTitle(gui,"lwtv")
bkg=wx.Panel(gui)
listbox0=wx.ListBox(bkg)
listbox1=wx.ListBox(bkg)
listbox2=wx.ListBox(bkg)

listbox0.Bind(wx.EVT_LEFT_UP,Setlist)
listbox1.Bind(wx.EVT_LEFT_UP,SetBlist)
listbox2.Bind(wx.EVT_LEFT_DCLICK,Open)

box=wx.BoxSizer()
box.Add(listbox0,proportion=1,flag=wx.EXPAND)
box.Add(listbox1,proportion=1,flag=wx.EXPAND)
box.Add(listbox2,proportion=1,flag=wx.EXPAND)
bkg.SetSizer(box)
gui.Centre()
gui.Show()

wx.ListBox.InsertItems(listbox0,list0,0)

app.MainLoop()
