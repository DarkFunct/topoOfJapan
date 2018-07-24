#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
client = pymongo.MongoClient()
db = client['gaozhi']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':133.307642,'bottom': 33.488613,'top':33.679482,'right':133.837877}
city2={'left':133.307642,'bottom': 33.408613,'top':33.679482,'right':133.837877}
polygon = [{'longitude':133.307642,'latitude':33.498613},
           {'longitude':133.307642,'latitude':33.679482},
           {'longitude':133.837877,'latitude':33.679482},
           {'longitude':133.837877,'latitude':33.498613}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
# instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
# instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='gaozhi.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='gaozhi_dire.txt')
col_parent = db['parent']
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='高知.kml')