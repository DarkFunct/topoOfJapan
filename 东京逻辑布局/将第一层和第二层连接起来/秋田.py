#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
from Tokyo_logistic_topo.kml_tool import ITDKkml
client = pymongo.MongoClient()
col_second_node = client['itdk_level_new']['qiutian_txt']
file_name = './file/link_qiutian.kml'
fkml=open(file_name,'w')
paint=ITDKkml(fkml)
ggg=TokyoTopo()
paint.setting_line(line_color='ffff3ef3',line_width=1.2,line_hight_start=0,line_hight_end=80000,altitudeMode='relativeToGround')
paint.head()
db_name = ['qiutian']
for name in db_name:
    db = client[name]
    col_tree_node = db['tree_node']
    col_map = db['map_logi2loca']
    for node in col_tree_node.find():
        if len(node['connect'])>5:
            docu = col_map.find_one({'node_id':node['node_id']})
            if docu['in']:
                min_dis = 10000
                min_point={}
                for second_node in col_second_node.find():
                    dis=ggg.get_distance(start=docu['new'],end=second_node['new'])
                    if dis<min_dis:
                        min_dis=dis
                        min_point=second_node['new']
                paint.draw_edge(start=docu['new'],end=min_point)
paint.tail()
fkml.close()