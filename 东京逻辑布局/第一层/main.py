#-*- coding:utf-8 -*-
'''
从日本拓扑中提取出东京的连接关系
'''
import pymongo
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
instance = TokyoTopo()
#client = pymongo.MongoClient('mongodb://kb314:fzdwxxcl.314@121.49.99.14:30011')
client = pymongo.MongoClient()
col_orignal_edge = client['itdkall_info']['edge']#日本所有边
col_Tokyo_edge = client['Tokyo_logistic']['edge_2ip']#东京边
col_Tokyo_node = client['Tokyo_logistic']['node_2ip']#东京点
city={'left':139.2407294868936,'bottom':35.11414856596891,'top':36.5420248360459,'right':140.8770722805165}
polygon = [{'longitude':140.5693025574302,'latitude':36.25539216903631},
           {'longitude':139.7197922881968,'latitude':36.39677915444565},
           {'longitude':139.542716084842,'latitude':36.30601547791137},
           {'longitude':139.0185846190601,'latitude':36.5420248360459},
           {'longitude':138.90911616833476,'latitude':36.35277009982055},
           {'longitude':139.0549852124244,'latitude':36.20108541455132},
           {'longitude':139.2456099261259,'latitude':36.11235004812491},
           {'longitude':139.3113501317328,'latitude':35.8384523396204},
           {'longitude':139.2525181244327,'latitude':35.70299975255817},
           {'longitude':139.3899602950388,'latitude':35.31378042594701},
           {'longitude':139.6774712858233,'latitude':35.27949596327179},
           {'longitude':139.6898523022618,'latitude':35.45375980863846},
           {'longitude':139.96027554466967,'latitude':35.64312960230637},
           {'longitude':140.0747402462124,'latitude':35.54810518616807},
           {'longitude':139.8167596636642,'latitude':35.30433736772609},
           {'longitude':140.1410756887876,'latitude':35.11414856596891},
           {'longitude':140.3946731253275,'latitude':35.17390565904493},
           {'longitude':140.3951667582674,'latitude':35.3765759005783},
           {'longitude':140.4541942066179,'latitude':35.53351636775477},
           {'longitude':140.6474389102403,'latitude':35.68424168595445},
           {'longitude':140.7303554856929,'latitude':35.69033869217626},
           {'longitude':140.8770722805165,'latitude':35.69380435065049},
           {'longitude':140.66968403862,'latitude':35.97498387578634},
           {'longitude':140.5708037498037,'latitude':36.18338343190715}]
col_Tokyo_tree = client['Tokyo_logistic']['tree']
col_Tokyo_tree_node = client['Tokyo_logistic']['tree_node']
col_map = client['Tokyo_logistic']['map_logi2loca']
#instance.extract_tokyo(col_Tokyo_node=col_Tokyo_node,col_Tokyo_edge=col_Tokyo_edge,city=city,col_orignal_edge=col_orignal_edge)
#instance.tokyo2tree(col_Tokyo_node=col_Tokyo_node,col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map)
#instance.coor2japan(city=city,col_map=col_map)
col_parent = client['Tokyo_logistic']['parent']
#instance.leaf2star(col_Tokyo_tree_node=col_Tokyo_tree_node,col_Tokyo_tree=col_Tokyo_tree,col_map=col_map,col_parent=col_parent)
instance.delete_point_of_polygon(polygon=polygon,col_map=col_map)
instance.new_tree(col_Tokyo_tree=col_Tokyo_tree,col_Tokyo_tree_node=col_Tokyo_tree_node,col_map=col_map)
#instance.geneKML(col_Tokyo_tree=col_Tokyo_tree,col_map=col_map)
instance.geneKML_no_leaf(col_Tokyo_tree=col_Tokyo_tree,col_map=col_map,col_Tokyo_tree_node=col_Tokyo_tree_node,file_name=r'Tokyo_no_leaf.kml')