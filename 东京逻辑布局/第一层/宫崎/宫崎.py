#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
client = pymongo.MongoClient()
db = client['gongqi']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':130.2297,'bottom':30.74 ,'top':33.29,'right':131.58}
city2={'left':131.2297,'bottom':31.74 ,'top':32.29,'right':131.58}
polygon = [{'longitude':131.4615597,'latitude':31.790734},
           {'longitude':131.2217105,'latitude': 31.8342453},
           {'longitude':131.286419,'latitude': 32.2768983},
           {'longitude':131.563294,'latitude': 32.251231}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
# instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
# instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='gongqi.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='gongqi_dire.txt')
col_parent = db['parent']
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='gongqi.kml')