#-*- coding:utf-8 -*-
import pymongo
import re
client = pymongo.MongoClient()
col=client['教育科研网']['图中点']
col.drop()
f = open('./file/教育科研网_点.kml','r',encoding='utf-8')
str =str( f.readlines())
pattern = re.compile("<coordinates>(.*?)</coordinates>")
location_list = pattern.findall(str)
print(location_list,len(location_list))
for item in location_list:
    ii = item.split(',')
    docu = {'longitude':float(ii[0]),'latitude':float(ii[1])}
    col.insert_one(docu)