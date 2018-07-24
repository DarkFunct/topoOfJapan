#-*- coding:utf-8 -*-
from second_layer.layout import SecondTopo
import pymongo
client = pymongo.MongoClient()
orig_edge = client['itdkall_info']['edge_all']
db_result = client['itdk_level_new']
col_edge = db_result['xinwu_edge']
col_point = db_result['xinwu_point']
col_point_degree = db_result['xinwu_point_degree']
col_edge_degree = db_result['xinwu_edge_degree']
col_txt = db_result['xinwu_txt']
city_info = {'name':'xinwu','longitude':139.093627,'latitude':37.808642,'range':40,'degree':30}
instance = SecondTopo()
filename_txt='./file/xinwu_edge.txt'
filename_kml='./file/xinwu_第二层.kml'
rec_range = {'left':139.019835,'bottom':37.8298 ,'top':37.909333768,'right':139.187}
filename_dire = './file/xinwu_dire.txt'
# instance.take_out(col_edge=col_edge,city_info=city_info,edge_collection=orig_edge)
# instance.degree_statistic(col_point=col_point,col_edge=col_edge)
# instance.gt_degree(col_point_degree=col_point_degree,col_point=col_point,degree=city_info['degree'])
# instance.find_link(col_edge_degree=col_edge_degree,col_edge=col_edge,col_point_degree=col_point_degree)
# instance.edge2txt(col_txt=col_txt,filename=filename_txt,col_edge_degree=col_edge_degree)
instance.gene_KML(filename_KML=filename_kml,col_txt=col_txt,rec_range=rec_range,filename_dire=filename_dire,col_edge_degree=col_edge_degree)