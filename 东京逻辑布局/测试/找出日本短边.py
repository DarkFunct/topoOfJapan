#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo,ITDKkml
client = pymongo.MongoClient()
col_edge = client['itdkall_info']['edge_all']
col_edge_static = client['itdkall_info']['edge_static_short_200']
#找出日本所有边，以地理位置为端点
col_edge_static.drop()
i=0
erro=0
cacu_dis = TokyoTopo()
for edge in col_edge.find({},{'_id':0},no_cursor_timeout = True):
    try:
        dis=cacu_dis.get_distance(start=edge['start'],end=edge['end'])
        if dis<250 and dis>1:
            docu = {'start':{'longitude':edge['start']['longitude'],'latitude':edge['start']['latitude']},
                                           'end':{'longitude':edge['end']['longitude'],'latitude':edge['end']['latitude']}}
            flag=col_edge_static.find_one(docu)
            if not flag:
                col_edge_static.insert_one(docu)
    except:
        erro+=1
    finally:
        print(i)
        i+=1
print(erro)
filename_KML = './file/日本第二层短边.kml'
f=open(filename_KML,'w')
paint = ITDKkml(f)
paint.setting_line(line_color= 'ffb40014',line_hight_start=0,line_hight_end=0,line_width=1)
#paint.setting_point(icon_path='juanjo_Router.png',point_hight=80000,point_scale=0.5)
paint.head()
for edge in col_edge_static.find():
    paint.draw_edge(start=edge['start'],end=edge['end'])
paint.tail()
f.close()