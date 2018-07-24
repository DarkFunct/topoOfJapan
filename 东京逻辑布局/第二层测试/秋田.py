#-*- coding:utf-8 -*-
from second_layer.layout import SecondTopo
import pymongo
client = pymongo.MongoClient()
orig_edge = client['itdkall_info']['edge_all']
db_result = client['itdk_level_new']
col_edge = db_result['qiutian_edge']
col_point = db_result['qiutian_point']
col_point_degree = db_result['qiutian_point_degree']
col_edge_degree = db_result['qiutian_edge_degree']
col_txt = db_result['qiutian_txt']
city_info = {'name':'qiutian','longitude':140.137319,'latitude': 39.706476,'range':35,'degree':0}
instance = SecondTopo()
filename_txt='./file/qiutian_edge.txt'
filename_kml='./file/qiutian_第二层.kml'
rec_range = {'left':140.111061,'bottom':39.788513,'top':40.009885,'right':140.274864}
filename_dire = './file/qiutian_dire.txt'
# instance.take_out(col_edge=col_edge,city_info=city_info,edge_collection=orig_edge)
# instance.degree_statistic(col_point=col_point,col_edge=col_edge)
#instance.gt_degree(col_point_degree=col_point_degree,col_point=col_point,degree=city_info['degree'])
# instance.find_link(col_edge_degree=col_edge_degree,col_edge=col_edge,col_point_degree=col_point_degree)
# instance.edge2txt(col_txt=col_txt,filename=filename_txt,col_edge_degree=col_edge_degree)
instance.gene_KML(filename_KML=filename_kml,col_txt=col_txt,rec_range=rec_range,filename_dire=filename_dire,col_edge_degree=col_edge_degree)