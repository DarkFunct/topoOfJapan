#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
client = pymongo.MongoClient()
db = client['gangshan']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':133.534168,'bottom': 34.450546 ,'top': 34.940239,'right':134.203184}
city2={'left':133.534168,'bottom': 34.450546 ,'top': 34.756779,'right':134.203184}
polygon = [{'longitude':133.534168,'latitude':34.450546},
           {'longitude':133.534168,'latitude':34.756779},
           {'longitude':134.203184,'latitude':34.756779},
           {'longitude':134.203184,'latitude':34.450546}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
# instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
# instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='冈山.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='gangshan_dire.txt')
col_parent = db['parent']
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='冈山.kml')