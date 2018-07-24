#-*- coding:utf-8 -*-
from second_layer.layout import SecondTopo
import pymongo
client = pymongo.MongoClient()
orig_edge = client['itdkall_info']['edge_all']
db_result = client['itdk_level_new']
col_edge = db_result['Fukuoka_edge']
col_point = db_result['Fukuoka_point']
col_point_degree = db_result['Fukuoka_point_degree']
col_edge_degree = db_result['Fukuoka_edge_degree']
col_txt = db_result['Fukuoka_txt']
city_info = {'name':'Fukuoka','longitude':130.4025,'latitude':33.59,'range':130,'degree':200}
instance = SecondTopo()
filename_txt='./file/Fukuoka_edge.txt'
filename_kml='./file/Fukuoka.kml'
rec_range = {'left':129.874,'bottom':32.8577,'top':33.8819,'right':131.0156}
filename_dire = './file/Fukuoka_dire.txt'
# instance.take_out(col_edge=col_edge,city_info=city_info,edge_collection=orig_edge)
# instance.degree_statistic(col_point=col_point,col_edge=col_edge)
#instance.gt_degree(col_point_degree=col_point_degree,col_point=col_point,degree=city_info['degree'])
# instance.find_link(col_edge_degree=col_edge_degree,col_edge=col_edge,col_point_degree=col_point_degree)
# instance.edge2txt(col_txt=col_txt,filename=filename_txt,col_edge_degree=col_edge_degree)
instance.gene_KML(filename_KML=filename_kml,col_txt=col_txt,rec_range=rec_range,filename_dire=filename_dire,col_edge_degree=col_edge_degree)