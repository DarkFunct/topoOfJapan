#-*- coding:utf-8 -*-
import pymongo,xlrd
#将度分秒转化为小数
def trans(s):
    s=s.split()[0]
    duuu = s.split('°')
    du = duuu[0].replace('E','').replace('N','')
    fennn = duuu[1]
    fen = fennn.split('′')[0]
    miaooo = fennn.split('′')[1]
    miao = miaooo.split('″')[0]
    li = (float(miao)/60+float(fen))/60+float(du)
    return li
client = pymongo.MongoClient()
col=client['教育科研网']['300大学']
col.drop()
ExcelFile=xlrd.open_workbook(r'./file/中国教育科研网节点具体位置1.xlsx')
sheet=ExcelFile.sheet_by_index(1)
list_latitude=sheet.col_values(3)
list_longitude=sheet.col_values(4)
num=len(list_latitude)
i=1
while i<num:
    print(sheet.col_values(1)[i].split(),sheet.col_values(4)[i].split(),sheet.col_values(3)[i].split())
    longitude = trans(list_longitude[i])
    latitude = trans(list_latitude[i])
    col.insert_one({'longitude':longitude,'latitude':latitude})
    print(longitude,latitude)
    i+=1