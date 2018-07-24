#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
client = pymongo.MongoClient()
db = client['guangdao']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':132.139103,'bottom':34.062162 ,'top':34.618114,'right':133.022745}
city2={'left':132.311368,'bottom':34.210125 ,'top':34.569991,'right':132.94097}
polygon = [{'longitude':132.967139,'latitude':34.609163},
           {'longitude':132.967139,'latitude':34.248602},
           {'longitude':132.272309,'latitude': 34.248602},
           {'longitude':132.2723091,'latitude':34.561720}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
# instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
# instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='guangdao.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='guangdao_dire.txt')
col_parent = db['parent']
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='guangdao.kml')