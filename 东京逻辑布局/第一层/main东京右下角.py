#-*- coding:utf-8 -*-
'''
从日本拓扑中提取出东京的连接关系
'''
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
#client = pymongo.MongoClient('mongodb://kb314:fzdwxxcl.314@121.49.99.14:30011')
client = pymongo.MongoClient()
db = client['Tokyo_right_logistic']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':139.6901024260538,'bottom':34.97714815661376,'top':35.60539647512219,'right':140.4344550653783}
city2={'left':139.7901024260538,'bottom':34.97714815661376,'top':35.54539647512219,'right':140.4344550653783}
polygon = [{'longitude':140.0895771923318,'latitude':35.54539647512219},
           {'longitude':140.4344550653783,'latitude':35.51038037627598},
           {'longitude':140.3376055390262,'latitude':35.13403284490654},
           {'longitude':139.9267373782394,'latitude':34.97714815661376},
           {'longitude':139.7901024260538,'latitude':35.31320346710189}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
#instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
#instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='tree_data_right.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='PajekData_right.txt')
col_parent = db['parent']
#instance.leaf2star(col_Tokyo_tree_node=col_Tokyo_tree_node,col_Tokyo_tree=col_Tokyo_tree,col_map=col_map,col_parent=col_parent)
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
#instance.new_tree(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='Tokyo_right.kml')
#instance.geneKML_no_leaf(col_Tokyo_tree=col_Tokyo_tree,col_map=col_map,col_Tokyo_tree_node=col_Tokyo_tree_node,file_name=r'Tokyo_no_leaf_left.kml')