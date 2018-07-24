#-*- coding:utf-8 -*-
'''
从日本拓扑中提取出东京的连接关系
'''
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
#client = pymongo.MongoClient('mongodb://kb314:fzdwxxcl.314@121.49.99.14:30011')
client = pymongo.MongoClient()
db = client['Tokyo_left_logistic']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':138.78036417554015,'bottom':35.84868084207971,'top':36.75358387408292,'right':139.7615553311103}
city2={'left':138.8236417554015,'bottom':36.04868084207971,'top':36.55358387408292,'right':139.6815553311103}
polygon = [{'longitude':139.02923613694,'latitude':36.55358387408292},
           {'longitude':139.6815553311103,'latitude':36.26919653916509},
           {'longitude':139.6264966411399,'latitude':36.06446875961306},
           {'longitude':139.2768578458557,'latitude':36.04868084207971},
           {'longitude':138.8236417554015,'latitude':36.25754389893214}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
# instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
# instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='tree_data_left.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='PajekData_left.txt')
col_parent = db['parent']
instance.leaf2star(col_Tokyo_tree_node=col_Tokyo_tree_node,col_Tokyo_tree=col_Tokyo_tree,col_map=col_map,col_parent=col_parent)
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
#instance.new_tree(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='Tokyo_left.kml')
#instance.geneKML_no_leaf(col_Tokyo_tree=col_Tokyo_tree,col_map=col_map,col_Tokyo_tree_node=col_Tokyo_tree_node,file_name=r'Tokyo_no_leaf_left.kml')