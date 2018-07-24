#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
client = pymongo.MongoClient()
db = client['dafen']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':131.453184,'bottom':33.127639 ,'top':33.246904,'right':131.764707}
city2={'left':131.453184,'bottom':33.127639 ,'top':33.246904,'right':131.764707}
polygon = [{'longitude':131.453184,'latitude':33.127639},
           {'longitude':131.453184,'latitude':33.246904},
           {'longitude':131.764707,'latitude':33.246904},
           {'longitude':131.764707,'latitude':33.127639}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
# instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
# instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='dafen.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='dafen_dire.txt')
col_parent = db['parent']
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='dafen.kml')