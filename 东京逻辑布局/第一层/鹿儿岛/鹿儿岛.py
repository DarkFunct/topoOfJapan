#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
client = pymongo.MongoClient()
db = client['luerdao']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':130.389277,'bottom':31.414848,'top':31.810341,'right':130.589483}
city2={'left':130.389277,'bottom':31.414848,'top':31.810341,'right':130.589483}
polygon = [{'longitude':130.389277,'latitude':31.414848},
           {'longitude':130.389277,'latitude':31.810341},
           {'longitude':130.589483,'latitude':31.810341},
           {'longitude':130.589483,'latitude':31.414848}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='luerdao.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='luerdao_dire.txt')
col_parent = db['parent']
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.new_tree(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map)
instance.geneKML_no_leaf(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='鹿儿岛.kml')