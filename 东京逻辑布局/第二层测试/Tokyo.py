#-*- coding:utf-8 -*-
from second_layer.layout import SecondTopo
import pymongo
client = pymongo.MongoClient()
orig_edge = client['itdkall_info']['edge_all']
db_result = client['itdk_level_new']
col_edge = db_result['Tokyo_edge']
col_point = db_result['Tokyo_point']
col_point_degree = db_result['Tokyo_point_degree']
col_edge_degree = db_result['Tokyo_edge_degree']
col_txt = db_result['Tokyo_txt']
city_info = {'name':'Tokyo','longitude':139.69194,'latitude':35.6894,'range':145,'degree':2500}
instance = SecondTopo()
filename_txt='./file/Tokyo_edge.txt'
filename_kml='./file/Tokyo.kml'
rec_range = {'left':139.29,'bottom':35.4177,'top':36.3719,'right':140.5656}
filename_dire = './file/Tokyo_dire.txt'
# instance.take_out(col_edge=col_edge,city_info=city_info,edge_collection=orig_edge)
# instance.degree_statistic(col_point=col_point,col_edge=col_edge)
#instance.gt_degree(col_point_degree=col_point_degree,col_point=col_point,degree=city_info['degree'])
#instance.find_link(col_edge_degree=col_edge_degree,col_edge=col_edge,col_point_degree=col_point_degree)
#instance.edge2txt(col_txt=col_txt,filename=filename_txt,col_edge_degree=col_edge_degree)
instance.gene_KML(filename_KML=filename_kml,col_txt=col_txt,rec_range=rec_range,filename_dire=filename_dire,col_edge_degree=col_edge_degree)