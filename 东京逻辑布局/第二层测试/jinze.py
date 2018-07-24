#-*- coding:utf-8 -*-
from second_layer.layout import SecondTopo
import pymongo
client = pymongo.MongoClient()
orig_edge = client['itdkall_info']['edge_all']
db_result = client['itdk_level_new']
col_edge = db_result['jinze_edge']
col_point = db_result['jinze_point']
col_point_degree = db_result['jinze_point_degree']
col_edge_degree = db_result['jinze_edge_degree']
col_txt = db_result['jinze_txt']
city_info = {'name':'jinze','longitude':136.93194,'latitude':36.6581,'range':56,'degree':50}
instance = SecondTopo()
filename_txt='./file/jinze_edge.txt'
filename_kml='./file/jinze.kml'
rec_range = {'left':136.59,'bottom':36.507,'top':36.819,'right':137.4256}
filename_dire = './file/jinze_dire.txt'
# instance.take_out(col_edge=col_edge,city_info=city_info,edge_collection=orig_edge)
# instance.degree_statistic(col_point=col_point,col_edge=col_edge)
# instance.gt_degree(col_point_degree=col_point_degree,col_point=col_point,degree=city_info['degree'])
# instance.find_link(col_edge_degree=col_edge_degree,col_edge=col_edge,col_point_degree=col_point_degree)
# instance.edge2txt(col_txt=col_txt,filename=filename_txt,col_edge_degree=col_edge_degree)
instance.gene_KML(filename_KML=filename_kml,col_txt=col_txt,rec_range=rec_range,filename_dire=filename_dire,col_edge_degree=col_edge_degree)