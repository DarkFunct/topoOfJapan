#-*- coding:utf-8 -*-
'''
从日本拓扑中提取出东京的连接关系
'''
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
#client = pymongo.MongoClient('mongodb://kb314:fzdwxxcl.314@121.49.99.14:30011')
client = pymongo.MongoClient()
db = client['Tokyo_leftdown_logistic']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':137.6830770474682,'bottom':35.27848918550292,'top':36.76996236057688,'right':139.625875496657}
city2={'left':139.1199746227325,'bottom':35.25735973013384,'top':36.05993049070996,'right':139.7952979334208}
polygon = [{'longitude':139.323717988167,'latitude':36.05993049070996},
           {'longitude':139.7952979334208,'latitude':35.96217128924244},
           {'longitude':139.541217788369,'latitude':35.30327189872084},
           {'longitude':139.1199746227325,'latitude':35.25735973013384}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
#instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
#instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='tree_data_left_down.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='PajekData_left_down.txt')
col_parent = db['parent']
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='Tokyo_left_down.kml')
