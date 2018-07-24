#-*- coding:utf-8 -*-
from second_layer.layout import SecondTopo
import pymongo
client = pymongo.MongoClient()
orig_edge = client['itdkall_info']['edge_all']
db_result = client['itdk_level_new']
col_edge = db_result['Nagoya_edge']
col_point = db_result['Nagoya_point']
col_point_degree = db_result['Nagoya_point_degree']
col_edge_degree = db_result['Nagoya_edge_degree']
col_txt = db_result['Nagoya_txt']
city_info = {'name':'Nagoya','longitude':136.9064,'latitude':35.1806,'range':60,'degree':500}
instance = SecondTopo()
filename_txt='./file/Nagoya_edge.txt'
filename_kml='./file/Nagoya.kml'
rec_range = {'left':136.564,'bottom':34.7577,'top':35.5419,'right':137.7256}
filename_dire = './file/Nagoya_dire.txt'
#instance.take_out(col_edge=col_edge,city_info=city_info,edge_collection=orig_edge)
#instance.degree_statistic(col_point=col_point,col_edge=col_edge)
# instance.gt_degree(col_point_degree=col_point_degree,col_point=col_point,degree=city_info['degree'])
# instance.find_link(col_edge_degree=col_edge_degree,col_edge=col_edge,col_point_degree=col_point_degree)
# instance.edge2txt(col_txt=col_txt,filename=filename_txt,col_edge_degree=col_edge_degree)
instance.gene_KML(filename_KML=filename_kml,col_txt=col_txt,rec_range=rec_range,filename_dire=filename_dire,col_edge_degree=col_edge_degree)