#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
client = pymongo.MongoClient()
db = client['jinze_left']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':135.998844,'bottom':35.896376,'top':36.262331,'right':136.479672}
city2={'left':135.998844,'bottom':35.896376,'top':36.262331,'right':136.479672}
polygon = [{'longitude':135.998844,'latitude':36.262331},
           {'longitude':135.998844,'latitude':35.896376},
           {'longitude':136.479672,'latitude':35.896376},
           {'longitude':136.479672,'latitude':36.2623312}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
# instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
# instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='jinze_left.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='dire_jinze_left.txt')
col_parent = db['parent']
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='jinze_left.kml')