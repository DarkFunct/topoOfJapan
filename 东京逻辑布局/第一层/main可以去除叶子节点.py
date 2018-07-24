#-*- coding:utf-8 -*-
'''
从日本拓扑中提取出东京的连接关系
'''
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
#client = pymongo.MongoClient('mongodb://kb314:fzdwxxcl.314@121.49.99.14:30011')
client = pymongo.MongoClient()
db = client['Tokyo_top_straight_haha_logistic']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':139.7141060655066,'bottom':36.35769222069168 ,'top':37.08784030782886,'right':140.2116932667467}
city2={'left':139.67972025601,'bottom':36.31095965970943 ,'top':36.82717099293689,'right':140.3060601170713}
polygon = [{'longitude':139.7646974057792,'latitude':36.82717099293689},
           {'longitude':140.3060601170713,'latitude':36.71236722257246},
           {'longitude':140.2128606224743,'latitude':36.31095965970943},
           {'longitude':139.679720256011,'latitude':36.37182624266654}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='tree_data_top_straight.txt')
#第二部分
instance.coor2japan(city=city2,col_map=col_map,txt_name='Pajektopstraight.txt')
col_parent = db['parent']
instance.leaf2star(col_Tokyo_tree_node=col_Tokyo_tree_node,col_Tokyo_tree=col_Tokyo_tree,col_map=col_map,col_parent=col_parent)
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.new_tree(col_Tokyo_tree_node=col_Tokyo_tree_node,col_Tokyo_tree=col_Tokyo_tree,col_map=col_map)
instance.geneKML_no_leaf(col_Tokyo_tree=col_Tokyo_tree,col_map=col_map,col_Tokyo_tree_node=col_Tokyo_tree_node,file_name='haha.kml')