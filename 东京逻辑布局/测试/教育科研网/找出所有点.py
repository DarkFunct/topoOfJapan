#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.kml_tool import ITDKkml
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
client = pymongo.MongoClient()
col_edge_degree = client['教育科研网']['node']#边

filename_KML = './教育科研网_点.kml'
f=open(filename_KML,'w')
paint = ITDKkml(f)
#paint.setting_line(line_hight_start=40000,line_hight_end=40000,line_width=5)
#paint.setting_point(icon_path='juanjo_Router.png',point_hight=80000,point_scale=0.5)
paint.head()
for node in col_edge_degree.find():
    paint.draw_orig_point(longitude=node['longitude'],latitude=node['latitude'])
paint.tail()
f.close()
