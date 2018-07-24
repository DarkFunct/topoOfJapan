#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
client = pymongo.MongoClient()
db = client['wuqu']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':134.065446,'bottom': 35.382537 ,'top': 35.561302,'right':134.452557}
city2={'left':134.065446,'bottom': 35.286108 ,'top': 35.551068,'right':134.376364}
polygon = [{'longitude':134.065446,'latitude':35.286108},
           {'longitude':134.065446,'latitude':35.56130},
           {'longitude':134.452554,'latitude':35.56130},
           {'longitude':134.45255,'latitude':35.286108}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
#instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
# instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='乌取.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='wuqu_dire.txt')
col_parent = db['parent']
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='乌取.kml')