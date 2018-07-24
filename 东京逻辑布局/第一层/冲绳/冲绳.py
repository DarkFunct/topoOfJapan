#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
client = pymongo.MongoClient()
db = client['chongsheng']
col_orignal_edge = client['itdkall_info']['edge_all']#日本所有边
col_Tokyo_edge = db['edge_2ip']#东京边
col_Tokyo_node = db['node_2ip']#东京点
city={'left':126.709620,'bottom': 26.069463 ,'top': 27.339153,'right':129.008637}
city2={'left':127.643642,'bottom':26.071788 ,'top':26.426301,'right':127.850209}
polygon = [{'longitude':127.8657612669696,'latitude':26.13483698438625},
           {'longitude':127.6811176008339,'latitude':26.06038880876092},
           {'longitude':127.6294172666856,'latitude':26.08176593884921},
           {'longitude':127.6181178168656,'latitude':26.21042340556956},
           {'longitude':127.7987975740686,'latitude':26.4729048714229},
            {'longitude':127.9965281581378,'latitude':26.38011224364966}]
col_Tokyo_tree = db['tree']
col_Tokyo_tree_node = db['tree_node']
col_map = db['map_logi2loca']
# instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
# instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file='chongsheng.txt')
instance.coor2japan(city=city2,col_map=col_map,txt_name='chongsheng_dire.txt')
col_parent = db['parent']
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map,file_name='chongsheng.kml')