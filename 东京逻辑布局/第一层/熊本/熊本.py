#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
client = pymongo.MongoClient()
db = client['xiongben']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':130.360180,'bottom':32.507063,'top':33.159971,'right':131.102055}
city2={'left':130.591893,'bottom':32.4527861,'top':33.084145,'right':131.046002}
polygon = [{'longitude':130.591893,'latitude':32.4527861},
           {'longitude':130.5918930,'latitude':33.084145},
           {'longitude':131.046002,'latitude': 33.084145},
           {'longitude':131.046002,'latitude':32.4527861}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
# instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
# instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='xiongben.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='xiongben_dire.txt')
col_parent = db['parent']
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='xiongben.kml')