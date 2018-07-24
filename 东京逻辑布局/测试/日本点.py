#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo,ITDKkml
client = pymongo.MongoClient()
iii=TokyoTopo()
col_edge1 = client['itdkall_info']['edge_location_degree']
col_edge2 = client['itdkall_info']['edge_static_short_250']

node11 =  client['itdkall_info']['日本第二层的点']
# node11.drop()
# for edge in col_edge1.find():
#     flag = node11.find_one(edge['start'])
#     if not flag:
#         node11.insert_one(edge['start'])
#     flag = node11.find_one(edge['end'])
#     if not flag:
#         node11.insert_one(edge['end'])
# for edge in col_edge2.find():
#     flag = node11.find_one(edge['start'])
#     if not flag:
#         node11.insert_one(edge['start'])
#     flag = node11.find_one(edge['end'])
#     if not flag:
#         node11.insert_one(edge['end'])
# print(node11.count())
filename_KML = './日本筛选后未处理所有点.kml'
f=open(filename_KML,'w')
paint = ITDKkml(f)
#paint.setting_line(line_hight_start=40000,line_hight_end=40000,line_width=5)
paint.setting_point(icon_path='juanjo_Router.png',point_hight=80000,point_scale=0.5)
paint.head()
for node in node11.find():
    paint.draw_orig_point(longitude=node['longitude'],latitude=node['latitude'])
paint.tail()
f.close()
