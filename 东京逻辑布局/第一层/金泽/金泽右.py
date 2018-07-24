#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
client = pymongo.MongoClient()
db = client['jinze_right']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':136.8773335808601,'bottom':36.49624084729228 ,'top':36.76917044223338,'right':137.436950362798}
city2={'left':136.8773335808601,'bottom':36.49624084729228 ,'top':36.76917044223338,'right':137.436950362798}
polygon = [{'longitude':137.4218369737113,'latitude':36.75345372483243},
           {'longitude':136.8773335808601,'latitude':36.76917044223338},
           {'longitude':136.8784072676285,'latitude':36.49624084729228},
           {'longitude':137.384933195871,'latitude':36.57309384282262}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
# instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
# instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='jinze_right.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='dire_jinze_right.txt')
col_parent = db['parent']
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='jinze_right.kml')