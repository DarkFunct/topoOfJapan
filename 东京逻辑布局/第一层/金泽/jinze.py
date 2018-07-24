#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
client = pymongo.MongoClient()
db = client['jinze']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':136.335642227407,'bottom':36.36336780402993 ,'top':36.9054095983338,'right':137.436950362798}
city2={'left':136.335642227407,'bottom':36.36336780402993 ,'top':36.9054095983338,'right':137.043695036279}
polygon = [{'longitude':136.7741081310587,'latitude':36.9054095983338},
           {'longitude':136.3356422274075,'latitude':36.36336780402993},
           {'longitude':137.436950362798,'latitude':36.60520135863723},
           {'longitude':137.3767301275331,'latitude':36.78050958658395},
           {'longitude':137.1122860874214,'latitude':36.77379878379396},
           {'longitude':136.9916,'latitude':36.8656},
           {'longitude':136.9916,'latitude':37.0599878379396}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
# instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
# instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='jinze.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='dire_jinze.txt')
col_parent = db['parent']
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='jinze.kml')