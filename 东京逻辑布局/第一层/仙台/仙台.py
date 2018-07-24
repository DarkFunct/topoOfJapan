#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
client = pymongo.MongoClient()
db = client['xiantai']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':140.1870668950105,'bottom':37.77120835568391 ,'top':38.72766513275968,'right':141.4196867813584}
city2={'left':140.61778950105,'bottom':38.005455683991 ,'top':38.4049333768,'right':141.149686781358}
polygon = [{'longitude':140.920758784351,'latitude':38.00545568391},
           {'longitude':140.61778950105,'latitude':38.00545568391},
           {'longitude':140.61778950105,'latitude':38.4049333753},
           {'longitude':141.1496867813584,'latitude':38.4049333753}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
# instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
# instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='xiantai.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='dire_xiantai.txt')
col_parent = db['parent']
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='xiantai.kml')