#!/usr/bin/python
#coding:utf-8

player="vlc"
weizhi="未知"

from Class import TvList
from Class import ValueList
from Class import ListValueList


from type import shaanxi
from type import letv
from type import itv
from type import tianwei
from type import qq
from type import qqgq
from type import xian
#CCTV
CCTV1=TvList()
CCTV1.SetName("CCTV1")
CCTV1.TypeAdd(tianwei,"TWSX0004200211100000")
CCTV2=TvList()
CCTV2.SetName("CCTV2")
CCTV2.TypeAdd(letv,"cctv2")
CCTV2.TypeAdd(itv,"cctv2")
CCTV3=TvList()
CCTV3.SetName("CCTV3")
CCTV3.TypeAdd(letv,"cctv3")
CCTV3.TypeAdd(itv,"cctv3")
CCTV4=TvList()
CCTV4.SetName("CCTV4")
CCTV4.TypeAdd(letv,"cctv4")
CCTV4.TypeAdd(itv,"cctv4")
CCTV5=TvList()
CCTV5.SetName("CCTV5")
CCTV5.TypeAdd(itv,"cctv5")
CCTV6=TvList()
CCTV6.SetName("CCTV6")
CCTV6.TypeAdd(letv,"cctv6")
CCTV6.TypeAdd(itv,"cctv6")
CCTV7=TvList()
CCTV7.SetName("CCTV7")
CCTV7.TypeAdd(letv,"cctv7")
CCTV7.TypeAdd(itv,"cctv7")
CCTV8=TvList()
CCTV8.SetName("CCTV8")
CCTV8.TypeAdd(letv,"cctv8")
CCTV9=TvList()
CCTV9.SetName("CCTV9")
CCTV9.TypeAdd(letv,"cctv9")
CCTV10=TvList()
CCTV10.SetName("CCTV10")
CCTV10.TypeAdd(letv,"cctv10")
CCTV10.TypeAdd(itv,"cctv10")
CCTV11=TvList()
CCTV11.SetName("CCTV11")
CCTV11.TypeAdd(letv,"cctv11")
CCTV11.TypeAdd(itv,"cctv11")
CCTV12=TvList()
CCTV12.SetName("CCTV12")
CCTV12.TypeAdd(letv,"cctv12")
CCTV12.TypeAdd(itv,"cctv12")
CCTV13=TvList()
CCTV13.SetName("CCTV13")
CCTV13.TypeAdd(letv,"cctvnew")
CCTV14=TvList()
CCTV14.SetName("CCTV14")
CCTV14.TypeAdd(letv,"cctvshaoer")
CCTV15=TvList()
CCTV15.SetName("CCTV15")
CCTV15.TypeAdd(letv,"cctvmusic")
fengyunyinyue=TvList()
fengyunyinyue.SetName("风云音乐")
fengyunyinyue.TypeAdd(letv,"cctvmusic")
guofangjunshi=TvList()
guofangjunshi.SetName("国防军事")
guofangjunshi.TypeAdd(letv,"guofangjunshi")
fengyunzuqiu=TvList()
fengyunzuqiu.SetName("风云足球")
fengyunzuqiu.TypeAdd(letv,"fyzq")


#北京
beijing_ws=TvList()
beijing_ws.SetName("北京卫视")
beijing_ws.TypeAdd(letv,"bjws")

beijing_tiyu=TvList()
beijing_tiyu.SetName("北京体育")
beijing_tiyu.TypeAdd(letv,"btv6_800")



#天津
tianjin_ws=TvList()
tianjin_ws.SetName("天津卫视")
tianjin_ws.TypeAdd(qq,"830075195")
tianjin_ws.TypeAdd(letv,"tianjin")

#上海
shanghai_ws=TvList()
shanghai_ws.SetName("东方卫视")
shanghai_ws.TypeAdd(qq,"3661744838")
shanghai_ws.TypeAdd(qqgq,"3900155972")
shanghai_ws.TypeAdd(letv,"dongfang")


shanghai_tiyu=TvList()
shanghai_tiyu.SetName("上海体育")
shanghai_tiyu.TypeAdd(letv,"shanghaitiyu_800")


#重庆
chongqing_ws=TvList()
chongqing_ws.SetName("重庆卫视")
chongqing_ws.TypeAdd(qq,"2905421066")
chongqing_ws.TypeAdd(letv,"chongqing")

#河北
hebei_ws=TvList()
hebei_ws.SetName("河北卫视")
hebei_ws.Add(player,"http://live01.hebtv.com/channels/hebtv/video_channel_ws4/flv:800k/live",weizhi,weizhi)
hebei_ws.TypeAdd(letv,"hebei")

#河南
henan_ws=TvList()
henan_ws.SetName("河南卫视")
henan_ws.TypeAdd(qq,"4172356212")
henan_ws.TypeAdd(letv,"henan")

#云南
yunnan_ws=TvList()
yunnan_ws.SetName("云南卫视")
yunnan_ws.TypeAdd(qq,"708402866")
yunnan_ws.TypeAdd(letv,"yunnan")

#辽宁
liaoning_ws=TvList()
liaoning_ws.SetName("辽宁卫视")
liaoning_ws.TypeAdd(qq,"3006271240")
liaoning_ws.TypeAdd(letv,"liaoning")

#黑龙江
heilongjiang_ws=TvList()
heilongjiang_ws.SetName("黑龙江卫视")
heilongjiang_ws.Add(player,"http://vtime.cntv.chinacache.net:8000/live/flv/channel99",weizhi,weizhi)
heilongjiang_ws.TypeAdd(letv,"heilongjiang")


#湖南
hunan_ws=TvList()
hunan_ws.SetName("湖南卫视")
hunan_ws.Add(player,"http://live-cdn.kksmg.com/channels/tvie/test/flv:500k",weizhi,weizhi)
hunan_ws.TypeAdd(letv,"hunan")

#安徽
anhui_ws=TvList()
anhui_ws.SetName("安徽卫视")
anhui_ws.TypeAdd(qq,"623043810")
anhui_ws.TypeAdd(letv,"anhui")

#山东
shandong_ws=TvList()
shandong_ws.SetName("山东卫视")
shandong_ws.TypeAdd(qq,"3660187036")
shandong_ws.TypeAdd(letv,"shandong")

#新疆
xinjiang_ws=TvList()
xinjiang_ws.SetName("新疆卫视")
xinjiang_ws.Add(player,"http://218.202.219.67/channels/xjyx/XJTV1-Envivio/flv:300k_rtmp",weizhi,weizhi)
xinjiang_ws.TypeAdd(letv,"xinjiang")

#江苏
jiangsu_ws=TvList()
jiangsu_ws.SetName("江苏卫视")
jiangsu_ws.Add(player,"rtmp://wwws.cietv.com/livestream/2ae90f52c9d90a319d6dcaadeb49844a",weizhi,weizhi)
jiangsu_ws.TypeAdd(letv,"jiangsu")

#浙江
zhejiang_ws=TvList()
zhejiang_ws.SetName("浙江卫视")
zhejiang_ws.TypeAdd(qq,"2907109968")
zhejiang_ws.TypeAdd(qqgq,"1975434150")
zhejiang_ws.TypeAdd(letv,"zhejiang")

#江西
jiangxi_ws=TvList()
jiangxi_ws.SetName("江西卫视")
jiangxi_ws.Add(player,"rtsp://tv.jxgdw.com/jxtv1",weizhi,weizhi)
jiangxi_ws.TypeAdd(letv,"jiangsu")

#湖北
hubei_ws=TvList()
hubei_ws.SetName("湖北卫视")
hubei_ws.TypeAdd(qq,"1128831868")
hubei_ws.TypeAdd(letv,"hubei")

#广西
guangxi_ws=TvList()
guangxi_ws.SetName("广西卫视")
guangxi_ws.TypeAdd(qq,"974433428")
guangxi_ws.TypeAdd(letv,"guangxi")


#甘肃
gansu_ws=TvList()
gansu_ws.SetName("甘肃卫视")
gansu_ws.TypeAdd(qq,"3444760127")
gansu_ws.TypeAdd(letv,"gansu")

#山西
shanxi_ws=TvList()
shanxi_ws.SetName("山西卫视")
shanxi_ws.TypeAdd(letv,"shanxi")

#muzhaodao

#内蒙古
neimenggu_ws=TvList()
neimenggu_ws.SetName("内蒙古卫视")
neimenggu_ws.TypeAdd(qq,"2342060367")
neimenggu_ws.TypeAdd(letv,"neimenggu")

#陕西
shaanxi_ws=TvList()
shaanxi_ws.SetName("陕西卫视")
shaanxi_ws.TypeAdd(qq,"2739752321")
shaanxi_ws.TypeAdd(letv,"shanxi1")
shaanxi_ws.TypeAdd(shaanxi,"8")
shaanxi_1=TvList()
shaanxi_1.SetName("陕西新闻资讯")
shaanxi_1.TypeAdd(shaanxi,"1")
shaanxi_2=TvList()
shaanxi_2.SetName("陕西都市生活")
shaanxi_2.TypeAdd(shaanxi,"2")
shaanxi_3=TvList()
shaanxi_3.SetName("陕西经济")
shaanxi_3.TypeAdd(shaanxi,"3")
shaanxi_5=TvList()
shaanxi_5.SetName("陕西公共")
shaanxi_5.TypeAdd(shaanxi,"5")
shaanxi_6=TvList()
shaanxi_6.SetName("陕西乐家购物")
shaanxi_6.TypeAdd(shaanxi,"6")
shaanxi_7=TvList()
shaanxi_7.SetName("陕西体育")
shaanxi_7.TypeAdd(shaanxi,"7")
shaanxi_9=TvList()
shaanxi_9.SetName("陕西农林卫视")
shaanxi_9.TypeAdd(shaanxi,"9")
xian_1=TvList()
xian_1.SetName("西安新闻综合")
xian_1.TypeAdd(xian,"DE9CFF32-E76C-11E0-BC3F-A10582DB7B64")
xian_2=TvList()
xian_2.SetName("西安都市频道")
xian_2.TypeAdd(xian,"0B153AA2-657E-11E0-9BC4-8191976A168D")
xian_3=TvList()
xian_3.SetName("西安商务资讯")
xian_3.TypeAdd(xian,"9971EE63-657E-11E0-9BC4-8191976A168D")
xian_4=TvList()
xian_4.SetName("西安文化影视")
xian_4.TypeAdd(xian,"678744E4-6597-11E0-9BC4-8191976A168D")
xian_5=TvList()
xian_5.SetName("西安健康快乐")
xian_5.TypeAdd(xian,"B24443C5-6597-11E0-9BC4-8191976A168D")
xian_6=TvList()
xian_6.SetName("西安音乐综艺")
xian_6.TypeAdd(xian,"E3922EB6-6597-11E0-9BC4-8191976A168D")

#吉林
jilin_ws=TvList()
jilin_ws.SetName("吉林卫视")
jilin_ws.TypeAdd(letv,"jilin")


#福建
dongnan_ws=TvList()
dongnan_ws.SetName("东南卫视")
dongnan_ws.TypeAdd(qq,"1000637964")
dongnan_ws.TypeAdd(letv,"dongnan")

#贵州
guizhou_ws=TvList()
guizhou_ws.SetName("贵州卫视")
guizhou_ws.TypeAdd(qq,"3051487004")
guizhou_ws.TypeAdd(letv,"guizhou")

#广东

guangdong_ws=TvList()
guangdong_ws.SetName("广东卫视")
guangdong_ws.TypeAdd(qq,"2084914015")
guangdong_ws.TypeAdd(qqgq,"857894899")
guangdong_ws.TypeAdd(letv,"guangdong")

shenzhen_ws=TvList()
shenzhen_ws.SetName("深圳卫视")
shenzhen_ws.TypeAdd(qq,"2309309351")
shenzhen_ws.TypeAdd(qqgq,"2220552576")
shenzhen_ws.TypeAdd(letv,"shenzhen")

nanfang_ws=TvList()
nanfang_ws.SetName("南方卫视")
nanfang_ws.TypeAdd(letv,"shenzhen")

guangdong_tiyu=TvList()
guangdong_tiyu.SetName("广东体育")
guangdong_tiyu.TypeAdd(letv,"guangdongtiyu")


#青海
qinghai_ws=TvList()
qinghai_ws.SetName("青海卫视")
qinghai_ws.TypeAdd(qq,"877636586")
qinghai_ws.TypeAdd(letv,"qinghai")

#西藏
xizang_ws=TvList()
xizang_ws.SetName("西藏卫视")
xizang_ws.TypeAdd(letv,"xizang")

#四川
sichuan_ws=TvList()
sichuan_ws.SetName("四川卫视")
sichuan_ws.TypeAdd(qq,"2453801339")
sichuan_ws.TypeAdd(letv,"sichuan")

#宁夏
ningxia_ws=TvList()
ningxia_ws.SetName("宁夏卫视")
ningxia_ws.TypeAdd(qq,"3778086045")
ningxia_ws.TypeAdd(letv,"ningxia")
#海南

#台湾

#香港
xianggang_ws=TvList()
xianggang_ws.SetName("香港卫视")
xianggang_ws.Add(player,"rtmp://live.hkstv.hk.lxdns.com/live/hks",weizhi,weizhi)
#澳门



#其他
lvyouweishi=TvList()
lvyouweishi.SetName("旅游卫视")
lvyouweishi.TypeAdd(letv,"lvyou")

fenghuangweishi=TvList()
fenghuangweishi.SetName("凤凰卫视")
fenghuangweishi.Add(player,"http://live.3gv.ifeng.com/live/FHZXHD.m3u8",weizhi,weizhi)

yataiweishi=TvList()
yataiweishi.SetName("亚太卫视")
yataiweishi.Add(player,"rtmp://58.61.150.198/live/Livestream",weizhi,weizhi)

jinbaotiyu=TvList()
jinbaotiyu.SetName("旅游卫视")
jinbaotiyu.TypeAdd(letv,"jingbaotiyu_800")

tianyuanweiqi=TvList()
tianyuanweiqi.SetName("天元围棋")
tianyuanweiqi.TypeAdd(letv,"tywq")

#----------------------------------------

List_CCTV=ValueList()
List_CCTV.SetThisName("央视")
List_CCTV.Add(CCTV1)
List_CCTV.Add(CCTV2)
List_CCTV.Add(CCTV3)
List_CCTV.Add(CCTV4)
List_CCTV.Add(CCTV5)
List_CCTV.Add(CCTV6)
List_CCTV.Add(CCTV7)
List_CCTV.Add(CCTV8)
List_CCTV.Add(CCTV9)
List_CCTV.Add(CCTV10)
List_CCTV.Add(CCTV11)
List_CCTV.Add(CCTV12)
List_CCTV.Add(CCTV13)
List_CCTV.Add(CCTV14)
List_CCTV.Add(CCTV15)
List_CCTV.Add(guofangjunshi)
List_CCTV.Add(fengyunyinyue)
List_CCTV.Add(fengyunzuqiu)


List_WS=ValueList()
List_WS.SetThisName("地方卫视")
List_WS.Add(beijing_ws)#北京
List_WS.Add(tianjin_ws)#天津
List_WS.Add(shanghai_ws)#上海
List_WS.Add(chongqing_ws)#重庆
List_WS.Add(hebei_ws)#河北
List_WS.Add(henan_ws)#河南
List_WS.Add(yunnan_ws)#云南
List_WS.Add(liaoning_ws)#辽宁
List_WS.Add(heilongjiang_ws)#黑龙江
List_WS.Add(hunan_ws)#湖南
List_WS.Add(anhui_ws)#安徽
List_WS.Add(shandong_ws)#山东
List_WS.Add(xinjiang_ws)#新疆
List_WS.Add(jiangsu_ws)#江苏
List_WS.Add(zhejiang_ws)#浙江
List_WS.Add(jiangxi_ws)#江西
List_WS.Add(hubei_ws)#湖北
List_WS.Add(guangxi_ws)#广西
List_WS.Add(gansu_ws)#甘肃
List_WS.Add(shanxi_ws)#山西
List_WS.Add(neimenggu_ws)#内蒙古
List_WS.Add(shaanxi_ws)#陕西
List_WS.Add(jilin_ws)#吉林
List_WS.Add(dongnan_ws)#福建
List_WS.Add(guizhou_ws)#贵州
List_WS.Add(guangdong_ws)#广东
List_WS.Add(shenzhen_ws)
List_WS.Add(nanfang_ws)
List_WS.Add(qinghai_ws)#青海
List_WS.Add(xizang_ws)#西藏
List_WS.Add(sichuan_ws)#四川
List_WS.Add(ningxia_ws)#宁夏
#海南
#台湾
List_WS.Add(xianggang_ws)#香港
#澳门
List_WS.Add(lvyouweishi)
List_WS.Add(fenghuangweishi)
List_WS.Add(yataiweishi)

#体育
List_tiyu=ValueList()
List_tiyu.SetThisName("体育")
List_tiyu.Add(guangdong_tiyu)
List_tiyu.Add(beijing_tiyu)
List_tiyu.Add(shanghai_tiyu)
List_tiyu.Add(jinbaotiyu)

#北京
List_beijing=ValueList()
List_beijing.SetThisName("北京")
List_beijing.Add(beijing_ws)

#天津
List_tianjin=ValueList()
List_tianjin.SetThisName("天津")
List_tianjin.Add(tianjin_ws)

#上海
List_shanghai=ValueList()
List_shanghai.SetThisName("上海")
List_shanghai.Add(shanghai_ws)
List_shanghai.Add(shanghai_tiyu)
#重庆
List_chongqing=ValueList()
List_chongqing.SetThisName("重庆")
List_chongqing.Add(chongqing_ws)

#河北
List_hebei=ValueList()
List_hebei.SetThisName("河北")
List_hebei.Add(hebei_ws)

#河南
List_henan=ValueList()
List_henan.SetThisName("河南")
List_henan.Add(henan_ws)

#云南
List_yunnan=ValueList()
List_yunnan.SetThisName("云南")
List_yunnan.Add(yunnan_ws)

#辽宁
List_liaoning=ValueList()
List_liaoning.SetThisName("辽宁")
List_liaoning.Add(liaoning_ws)

#黑龙江
List_heilongjiang=ValueList()
List_heilongjiang.SetThisName("黑龙江")
List_heilongjiang.Add(heilongjiang_ws)

#湖南
List_hunan=ValueList()
List_hunan.SetThisName("湖南")
List_hunan.Add(hunan_ws)

#安徽
List_anhui=ValueList()
List_anhui.SetThisName("安徽")
List_anhui.Add(anhui_ws)

#山东
List_shandong=ValueList()
List_shandong.SetThisName("山东")
List_shandong.Add(shandong_ws)

#新疆
List_xinjiang=ValueList()
List_xinjiang.SetThisName("新疆")
List_xinjiang.Add(xinjiang_ws)

#江苏
List_jiangsu=ValueList()
List_jiangsu.SetThisName("江苏")
List_jiangsu.Add(jiangsu_ws)

#浙江
List_zhejiang=ValueList()
List_zhejiang.SetThisName("浙江")
List_zhejiang.Add(zhejiang_ws)

#江西
List_jiangxi=ValueList()
List_jiangxi.SetThisName("江西")
List_jiangxi.Add(jiangxi_ws)

#湖北
List_hubei=ValueList()
List_hubei.SetThisName("湖北")
List_hubei.Add(hubei_ws)

#广西
List_guangxi=ValueList()
List_guangxi.SetThisName("广西")
List_guangxi.Add(guangxi_ws)

#甘肃
List_gansu=ValueList()
List_gansu.SetThisName("甘肃")
List_gansu.Add(gansu_ws)

#山西
List_shanxi=ValueList()
List_shanxi.SetThisName("山西")
List_shanxi.Add(shanxi_ws)

#内蒙古
List_neimenggu=ValueList()
List_neimenggu.SetThisName("内蒙古")
List_neimenggu.Add(neimenggu_ws)

#陕西
List_shaanxi=ValueList()
List_shaanxi.SetThisName("陕西")
List_shaanxi.Add(shaanxi_1)
List_shaanxi.Add(shaanxi_2)
List_shaanxi.Add(shaanxi_3)
List_shaanxi.Add(shaanxi_5)
List_shaanxi.Add(shaanxi_6)
List_shaanxi.Add(shaanxi_7)
List_shaanxi.Add(shaanxi_ws)
List_shaanxi.Add(xian_1)
List_shaanxi.Add(xian_2)
List_shaanxi.Add(xian_3)
List_shaanxi.Add(xian_4)
List_shaanxi.Add(xian_5)
List_shaanxi.Add(xian_6)

#吉林
List_jilin=ValueList()
List_jilin.SetThisName("吉林")
List_jilin.Add(jilin_ws)

#福建
List_fujian=ValueList()
List_fujian.SetThisName("福建")
List_fujian.Add(dongnan_ws)

#贵州
List_guizhou=ValueList()
List_guizhou.SetThisName("贵州")
List_guizhou.Add(guizhou_ws)

#广东
List_guangdong=ValueList()
List_guangdong.SetThisName("广东")
List_guangdong.Add(guangdong_ws)
List_guangdong.Add(shenzhen_ws)
List_guangdong.Add(nanfang_ws)
List_guangdong.Add(guangdong_tiyu)
#青海
List_qinghai=ValueList()
List_qinghai.SetThisName("青海")
List_qinghai.Add(qinghai_ws)

#西藏
List_xizang=ValueList()
List_xizang.SetThisName("青海")
List_xizang.Add(xizang_ws)

#四川
List_sichuan=ValueList()
List_sichuan.SetThisName("四川")
List_sichuan.Add(sichuan_ws)

#宁夏
List_ningxia=ValueList()
List_ningxia.SetThisName("宁夏")
List_ningxia.Add(ningxia_ws)

#海南

#台湾

#香港
List_xianggang=ValueList()
List_xianggang.SetThisName("香港")
List_xianggang.Add(xianggang_ws)

#澳门

#其他
List_qita=ValueList()
List_qita.SetThisName("其他")
List_qita.Add(lvyouweishi)
List_qita.Add(fenghuangweishi)
List_qita.Add(yataiweishi)
List_qita.Add(jinbaotiyu)
List_qita.Add(tianyuanweiqi)
#-----------------------------------
Tv=ListValueList()
Tv.Add(List_CCTV)
Tv.Add(List_WS)
Tv.Add(List_tiyu)
Tv.Add(List_beijing)#北京
Tv.Add(List_tianjin)#天津
Tv.Add(List_shanghai)#上海
Tv.Add(List_chongqing)#重庆
Tv.Add(List_hebei)#河北
Tv.Add(List_henan)#河南
Tv.Add(List_yunnan)#云南
Tv.Add(List_liaoning)#辽宁
Tv.Add(List_heilongjiang)#黑龙江
Tv.Add(List_hunan)#湖南
Tv.Add(List_anhui)#安徽
Tv.Add(List_shandong)#山东
Tv.Add(List_xinjiang)#新疆
Tv.Add(List_jiangsu)#江苏
Tv.Add(List_zhejiang)#浙江
Tv.Add(List_jiangxi)#江西
Tv.Add(List_hubei)#湖北
Tv.Add(List_guangxi)#广西
Tv.Add(List_gansu)#甘肃
Tv.Add(List_shanxi)#山西
Tv.Add(List_neimenggu)#内蒙古
Tv.Add(List_shaanxi)#陕西
Tv.Add(List_jilin)#吉林
Tv.Add(List_fujian)#福建
Tv.Add(List_guizhou)#贵州
Tv.Add(List_guangdong)#广东
Tv.Add(List_qinghai)#青海
Tv.Add(List_sichuan)#四川
Tv.Add(List_ningxia)#宁夏
#海南
#台湾
Tv.Add(List_xianggang)#香港
#澳门
Tv.Add(List_qita)#其他
