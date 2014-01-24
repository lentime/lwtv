#!/usr/bin/python
#coding:utf-8
import shlex
import webbrowser
import subprocess
from type import letv
from type import itv
from type import tianwei
from type import qq
from type import qqgq
meaulist=["央视","地方卫视"]



player="vlc"
brower="www"

class TvList():
    def __init__(self):
        self.Name=[]
        self.Url=[]
        self.Open=[]
    def Add(self,_Name,_Open,_Url):
        self.Name.append(_Name)
        self.Open.append(_Open)
        self.Url.append(_Url)
    def TypeAdd(self,value,value1):
        self.Name.append(value.GetName())
        self.Open.append(value.GetOpen())
        self.Url.append(value.GetUrl(value1))
    def Get(self,vlaue):
        if vlaue=="Name":
            return self.Name
        elif vlaue=="Url":
            return self.Url
        elif vlaue=="Open":
            return self.Open
    def OpenWith(self,value):
        if self.Open[value]=="www":
            webbrowser.open_new_tab(self.Url[value])
            return
        subprocess.Popen(shlex.split(self.Open[value]+" "+self.Url[value]))




CCTV1=TvList()
CCTV1.TypeAdd(tianwei,"TWSX0004200211100000")
CCTV2=TvList()
CCTV2.TypeAdd(letv,"cctv2")
CCTV3=TvList()
CCTV3.TypeAdd(letv,"cctv3")
CCTV4=TvList()
CCTV4.TypeAdd(letv,"cctv4")
CCTV5=TvList()
CCTV5.TypeAdd(itv,"cctv5")
CCTV6=TvList()
CCTV6.TypeAdd(letv,"cctv6")
CCTV7=TvList()
CCTV7.TypeAdd(letv,"cctv7")
CCTV8=TvList()
CCTV8.TypeAdd(letv,"cctv8")
CCTV9=TvList()
CCTV9.TypeAdd(letv,"cctv9")
CCTV10=TvList()
CCTV10.TypeAdd(letv,"cctv10")
CCTV11=TvList()
CCTV11.TypeAdd(letv,"cctv11")
CCTV12=TvList()
CCTV12.TypeAdd(letv,"cctv12")

ws_hb=TvList()
ws_hb.TypeAdd(qq,"1128831868")
ws_tj=TvList()
ws_tj.TypeAdd(qq,"830075195")
ws_dn=TvList()
ws_dn.TypeAdd(qq,"1000637964")
ws_ah=TvList()
ws_ah.TypeAdd(qq,"623043810")
ws_df=TvList()
ws_df.TypeAdd(qq,"3661744838")
ws_df.TypeAdd(qqgq,"3900155972")
ws_gd=TvList()
ws_gd.TypeAdd(qq,"2084914015")
ws_gd.TypeAdd(qqgq,"857894899")
ws_zj=TvList()
ws_zj.TypeAdd(qq,"2907109968")
ws_zj.TypeAdd(qqgq,"1975434150")
ws_gz=TvList()
ws_gz.TypeAdd(qq,"3051487004")
ws_sz=TvList()
ws_sz.TypeAdd(qq,"2309309351")
ws_sz.TypeAdd(qqgq,"2220552576")
ws_sc=TvList()
ws_sc.TypeAdd(qq,"2453801339")
ws_nm=TvList()
ws_nm.TypeAdd(qq,"2342060367")
ws_nx=TvList()
ws_nx.TypeAdd(qq,"3778086045")
ws_gs=TvList()
ws_gs.TypeAdd(qq,"3444760127")
ws_cq=TvList()
ws_cq.TypeAdd(qq,"2905421066")
ws_gx=TvList()
ws_gx.TypeAdd(qq,"974433428")
ws_henan=TvList()
ws_henan.TypeAdd(qq,"4172356212")
ws_yn=TvList()
ws_yn.TypeAdd(qq,"708402866")
ws_shaanxi=TvList()
ws_shaanxi.TypeAdd(qq,"2739752321")
ws_sd=TvList()
ws_sd.TypeAdd(qq,"3660187036")
ws_qh=TvList()
ws_qh.TypeAdd(qq,"877636586")
ws_ln=TvList()
ws_ln.TypeAdd(qq,"3006271240")
#第一个列表
def GetMeauList():
    return meaulist


CCTV=["CCTV1","CCTV2","CCTV3","CCTV4","CCTV5","CCTV6","CCTV7","CCTV8","CCTV9","CCTV10","CCTV11","CCTV12"]
CCTV_List=[CCTV1,CCTV2,CCTV3,CCTV4,CCTV5,CCTV6,CCTV7,CCTV8,CCTV9,CCTV10,CCTV11,CCTV12]
ws=["湖北卫视","天津卫视","东南卫视","安徽卫视","东方卫视","广东卫视","浙江卫视","贵州卫视","深圳卫视","四川卫视","内蒙古卫视","宁夏卫视","甘肃卫视","重庆卫视","广西卫视","河南卫视","云南卫视","陕西卫视","山东卫视","青海卫视","辽宁卫视"]
ws_List=[ws_hb,ws_tj,ws_dn,ws_ah,ws_df,ws_gd,ws_zj,ws_gz,ws_sz,ws_sc,ws_nm,ws_nx,ws_gs,ws_cq,ws_gx,ws_henan,ws_yn,ws_shaanxi,ws_sd,ws_qh,ws_ln]



#第二个列表
def GetTvList(value):
    if value==0:
        return CCTV
    elif value==1:
        return ws




#央视


#第三个列表参数读取或操作
def Change(value1,value2,value3,value4):
    if value1==0:
#央视
        if value3!=None:
            return CCTV_List[value2].Get(value3)
        if value4!=None:
            CCTV_List[value2].OpenWith(value4)
    elif value1==1:
        if value3!=None:
            return ws_List[value2].Get(value3)
        if value4!=None:
            ws_List[value2].OpenWith(value4)
        


    
