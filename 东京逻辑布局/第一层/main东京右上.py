#-*- coding:utf-8 -*-
'''
从日本拓扑中提取出东京的连接关系
'''
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
#client = pymongo.MongoClient('mongodb://kb314:fzdwxxcl.314@121.49.99.14:30011')
client = pymongo.MongoClient()
db = client['Tokyo_top_logistic']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':139.6901024260538,'bottom':36.26314775201392,'top':36.77127584715117,'right':140.6420862754152}
city2={'left':140.2169898949832,'bottom':36.25983049995579,'top':36.59847557386378,'right':140.6565614290742}
polygon = [{'longitude':140.2426378378081,'latitude':36.59847557386378},
           {'longitude':140.2169898949832,'latitude':36.28099751420809},
           {'longitude':140.5788756253149,'latitude':36.25983049995579},
           {'longitude':140.6565614290742,'latitude':36.55309693386927}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='tree_data_top.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='PajekData_top.txt')
col_parent = db['parent']
#instance.leaf2star(col_Tokyo_tree_node=col_Tokyo_tree_node,col_Tokyo_tree=col_Tokyo_tree,col_map=col_map,col_parent=col_parent)
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
#instance.new_tree(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='Tokyo_top.kml')
#instance.geneKML_no_leaf(col_Tokyo_tree=col_Tokyo_tree,col_map=col_map,col_Tokyo_tree_node=col_Tokyo_tree_node,file_name=r'Tokyo_no_leaf_left.kml')