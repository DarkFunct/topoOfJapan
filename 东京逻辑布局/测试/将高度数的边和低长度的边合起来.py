#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.kml_tool import ITDKkml
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo,ITDKkml
client = pymongo.MongoClient()
iii=TokyoTopo()
col_edge1 = client['itdkall_info']['edge_location_degree']
col_edge2 = client['itdkall_info']['edge_static_short_250']
#两类边合体
col_edge_merge = client['itdkall_info']['merge']
col_edge_merge.drop()
for edge in col_edge1.find():
    if iii.get_distance(start=edge['start'],end=edge['end'])<400:
        docu = {'start':{'longitude':edge['start']['longitude'],'latitude':edge['start']['latitude']},
                'end':{'longitude':edge['end']['longitude'], 'latitude':edge['end']['latitude']}}
        col_edge_merge.insert_one(docu)
for edge in col_edge2.find():
    docu = {'start':{'longitude':edge['start']['longitude'],'latitude':edge['start']['latitude']},
                'end':{'longitude':edge['end']['longitude'], 'latitude':edge['end']['latitude']}}
    flag = col_edge_merge.find_one(docu)
    if not flag:
        col_edge_merge.insert_one(docu)
filename_KML = './file/日本整个第二层merge.kml'
f=open(filename_KML,'w')
paint = ITDKkml(f)
paint.setting_line(line_color= 'ffb40014',line_hight_start=80000,line_hight_end=80000,line_width=1,altitudeMode='relativeToGround')
#paint.setting_point(icon_path='juanjo_Router.png',point_hight=80000,point_scale=0.5)
paint.head()
for edge in col_edge_merge.find():
    paint.draw_edge(start=edge['start'],end=edge['end'])
paint.tail()
f.close()