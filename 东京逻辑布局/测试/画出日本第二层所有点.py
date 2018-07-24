#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.kml_tool import ITDKkml
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
client = pymongo.MongoClient()
col_edge_degree = client['itdkall_info']['merge']#边
db = client['itdk_level_new']
#先将所有的城市转到一个集合中
col_second = db['point_second_layer']
col_point_second = db['point_second']
# col_point_second.drop()
# for edge in col_edge_degree.find():
#     node1 = edge['start']
#     flag = col_second.find_one({'longitude':node1['longitude'],'latitude':node1['latitude']})
#     if flag:
#         node1=flag['new']
#     flag2 = col_point_second.find_one({'longitude':node1['longitude'],'latitude':node1['latitude']})
#     if not flag2:
#         col_point_second.insert_one(node1)
#
#     node2 = edge['end']
#     flag = col_second.find_one({'longitude':node2['longitude'],'latitude':node2['latitude']})
#     if flag:
#         node2=flag['new']
#     flag2 = col_point_second.find_one({'longitude':node2['longitude'],'latitude':node2['latitude']})
#     if not flag2:
#         col_point_second.insert_one(node2)
#画图,dian
iii=TokyoTopo()
filename_KML = './file/日本整个第二层的点.kml'
f=open(filename_KML,'w')
paint = ITDKkml(f)
paint.setting_point(icon_path='juanjo_Router.png',point_hight=40000,point_scale=0.3,point_color='')
paint.head()
for node in col_point_second.find():
    paint.draw_point2(longitude=node['longitude'],latitude=node['latitude'])
paint.tail()
f.close()