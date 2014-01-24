#coding:utf-8
print "德马西亚"


class _letv():
    def GetName(self):
        return "乐视"
    def GetUrl(self,value):
        return "http://sports.letv.com/zt/hzsports262/index.html?streamid="+value+"&alsc=x0"
    def GetOpen(self,):
        return "www"
letv=_letv()

class _52itv():
    def GetName(self):
        return "52itv平台"
    def GetUrl(self,value):
        return "http://rtmp.cntv.lxdns.com/live/"+value+"/playlist.m3u8"
    def GetOpen(self,):
        return "vlc"
itv=_52itv()

class _tianwei():
    def GetName(self):
        return "天威"
    def GetUrl(self,value):
        return "http://116.77.70.81/live/1,"+value+"?format=mpegts&codec=x264&bitrate=1200k"
    def GetOpen(self,):
        return "vlc"
tianwei=_tianwei()

class _qq():
    def GetName(self):
        return "腾讯"
    def GetUrl(self,value):
        return "http://zb.v.qq.com:1863/?progid="+value
    def GetOpen(self,):
        return "vlc"
qq=_qq()

class _qqgq():
    def GetName(self):
        return "腾讯高清"
    def GetUrl(self,value):
        return "http://zb.v.qq.com:1863/?progid="+value
    def GetOpen(self,):
        return "vlc"
qqgq=_qqgq()



