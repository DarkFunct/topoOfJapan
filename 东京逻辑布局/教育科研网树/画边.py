#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.kml_tool import ITDKkml
client = pymongo.MongoClient()
col_edge_degree = client['教育科研网']['大学边']#边
col_point = client['教育科研网']['大学里面的点']#边
filename_KML = './教育科研网_大学边.kml'
f=open(filename_KML,'w')
paint = ITDKkml(f)
#paint.setting_line(line_hight_start=40000,line_hight_end=40000,line_width=5)
#paint.setting_point(icon_path='juanjo_Router.png',point_hight=80000,point_scale=0.5)
paint.head()
for edge in col_edge_degree.find():
    paint.draw_edge(start=edge['start'],end=edge['end'])
paint.tail()
f.close()

col_edge_leaf = client['教育科研网']['叶子边']
filename_KML = './教育科研网_大学叶子边.kml'
f=open(filename_KML,'w')
paint = ITDKkml(f)
#paint.setting_line(line_hight_start=40000,line_hight_end=40000,line_width=5)
#paint.setting_point(icon_path='juanjo_Router.png',point_hight=80000,point_scale=0.5)
paint.head()
for edge in col_edge_leaf.find():
    paint.draw_edge(start=edge['start'],end=edge['end'])
paint.tail()
f.close()

col_point_leaf = client['教育科研网']['叶子节点']
filename_KML = './教育科研网_大学里面的叶子点.kml'
f=open(filename_KML,'w')
paint = ITDKkml(f)
#paint.setting_line(line_hight_start=40000,line_hight_end=40000,line_width=5)
paint.setting_point(point_scale=0.3)
paint.head()
for node in col_point_leaf.find():
    paint.draw_orig_point(longitude=node['longitude'],latitude=node['latitude'])
paint.tail()
f.close()

col_point_leaf = client['教育科研网']['大学里面的点']
filename_KML = './教育科研网_大学里面点.kml'
f=open(filename_KML,'w')
paint = ITDKkml(f)
#paint.setting_line(line_hight_start=40000,line_hight_end=40000,line_width=5)
paint.setting_point(point_scale=0.3)
paint.head()
for node in col_point_leaf.find():
    paint.draw_orig_point(longitude=node['longitude'],latitude=node['latitude'])
paint.tail()
f.close()