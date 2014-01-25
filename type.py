#coding:utf-8
print "天天好心情"

player="vlc"
webbrowser="www"

weizhi="未知"

class _letv():
    def GetServeName(self):
        return "乐视 [支持回播]"
    def GetUrl(self,value):
        return "http://sports.letv.com/zt/hzsports262/index.html?streamid="+value+"&alsc=x0"
    def GetOpen(self,):
        return webbrowser
letv=_letv()

class _52itv():
    def GetServeName(self):
        return "52itv平台"
    def GetUrl(self,value):
        return "http://rtmp.cntv.lxdns.com/live/"+value+"/playlist.m3u8"
    def GetOpen(self,):
        return player
itv=_52itv()

class _tianwei():
    def GetServeName(self):
        return "天威"
    def GetUrl(self,value):
        return "http://116.77.70.81/live/1,"+value+"?format=mpegts&codec=x264&bitrate=1200k"
    def GetOpen(self,):
        return player
tianwei=_tianwei()

class _qq():
    def GetServeName(self):
        return "腾讯 [标清]"
    def GetUrl(self,value):
        return "http://zb.v.qq.com:1863/?progid="+value
    def GetOpen(self,):
        return player
qq=_qq()

class _qqgq():
    def GetServeName(self):
        return "腾讯 [高清]"
    def GetUrl(self,value):
        return "http://zb.v.qq.com:1863/?progid="+value
    def GetOpen(self,):
        return player
qqgq=_qqgq()

class _shaanxi():
    def GetServeName(self):
        return "陕西电视台 [流畅]"
    def GetUrl(self,value):
        return "mms://124.115.8.74/sxtvs-"+value
    def GetOpen(self,):
        return player
shaanxi=_shaanxi()

class _xian():
    def GetServeName(self):
        return weizhi+" [流畅]"
    def GetUrl(self,value):
        return "http://113.140.13.197/live/2011/03/03/"+value+"?fmt=x264_500k_flv&start=0"
    def GetOpen(self,):
        return player
xian=_xian()


