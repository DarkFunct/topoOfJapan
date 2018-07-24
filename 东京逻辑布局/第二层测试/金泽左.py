#-*- coding:utf-8 -*-
from second_layer.layout import SecondTopo
import pymongo
client = pymongo.MongoClient()
orig_edge = client['itdkall_info']['edge_all']
db_result = client['itdk_level_new']
col_edge = db_result['jinze_left_edge']
col_point = db_result['jinze_left_point']
col_point_degree = db_result['jinze_left_point_degree']
col_edge_degree = db_result['jinze_left_edge_degree']
col_txt = db_result['jinze_left_txt']
city_info = {'name':'jinze_left','longitude':136.214329,'latitude':36.007677,'range':40,'degree':20}
instance = SecondTopo()
filename_txt='./file/jinze_left_edge.txt'
filename_kml='./file/jinze_left.kml'
rec_range = {'left':135.998844,'bottom':35.896376,'top':36.262331,'right':136.479672}
filename_dire = './file/jinze_left_dire.txt'
# instance.take_out(col_edge=col_edge,city_info=city_info,edge_collection=orig_edge)
# instance.degree_statistic(col_point=col_point,col_edge=col_edge)
# instance.gt_degree(col_point_degree=col_point_degree,col_point=col_point,degree=city_info['degree'])
# instance.find_link(col_edge_degree=col_edge_degree,col_edge=col_edge,col_point_degree=col_point_degree)
# instance.edge2txt(col_txt=col_txt,filename=filename_txt,col_edge_degree=col_edge_degree)
instance.gene_KML(filename_KML=filename_kml,col_txt=col_txt,rec_range=rec_range,filename_dire=filename_dire,col_edge_degree=col_edge_degree)