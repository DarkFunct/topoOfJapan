#-*- coding:utf-8 -*-
from second_layer.layout import SecondTopo
import pymongo
client = pymongo.MongoClient()
orig_edge = client['itdkall_info']['edge_all']
db_result = client['itdk_level_new']
col_edge = db_result['changqi_edge']
col_point = db_result['changqi_point']
col_point_degree = db_result['changqi_point_degree']
col_edge_degree = db_result['changqi_edge_degree']
col_txt = db_result['changqi_txt']
city_info = {'name':'changqi','longitude':129.961416,'latitude': 32.790932,'range':20,'degree':1}
instance = SecondTopo()
filename_txt='./file/changqi_edge.txt'
filename_kml='./file/changqi_第二层.kml'
rec_range = {'left':129.882272,'bottom':32.77457,'top':32.834483,'right':130.033072}
filename_dire = './file/changqi_dire.txt'
# instance.take_out(col_edge=col_edge,city_info=city_info,edge_collection=orig_edge)
# instance.degree_statistic(col_point=col_point,col_edge=col_edge)
# instance.gt_degree(col_point_degree=col_point_degree,col_point=col_point,degree=city_info['degree'])
# instance.find_link(col_edge_degree=col_edge_degree,col_edge=col_edge,col_point_degree=col_point_degree)
# instance.edge2txt(col_txt=col_txt,filename=filename_txt,col_edge_degree=col_edge_degree)
instance.gene_KML(filename_KML=filename_kml,col_txt=col_txt,rec_range=rec_range,filename_dire=filename_dire,col_edge_degree=col_edge_degree)