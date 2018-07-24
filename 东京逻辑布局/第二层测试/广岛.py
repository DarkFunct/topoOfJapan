#-*- coding:utf-8 -*-
from second_layer.layout import SecondTopo
import pymongo
client = pymongo.MongoClient()
orig_edge = client['itdkall_info']['edge_all']
db_result = client['itdk_level_new']
col_edge = db_result['guangdao_edge']
col_point = db_result['guangdao_point']
col_point_degree = db_result['guangdao_point_degree']
col_edge_degree = db_result['guangdao_edge_degree']
col_txt = db_result['guangdao_txt']
city_info = {'name':'guangdao','longitude':132.471128,'latitude':34.392385,'range':35,'degree':0}
instance = SecondTopo()
filename_txt='./file/guangdao_edge.txt'
filename_kml='./file/guangdao_第二层.kml'
rec_range = {'left':132.639069,'bottom':34.246408 ,'top':34.474648,'right':132.916981}
filename_dire = './file/guangdao_dire.txt'
# instance.take_out(col_edge=col_edge,city_info=city_info,edge_collection=orig_edge)
# instance.degree_statistic(col_point=col_point,col_edge=col_edge)
# instance.gt_degree(col_point_degree=col_point_degree,col_point=col_point,degree=city_info['degree'])
# instance.find_link(col_edge_degree=col_edge_degree,col_edge=col_edge,col_point_degree=col_point_degree)
# instance.edge2txt(col_txt=col_txt,filename=filename_txt,col_edge_degree=col_edge_degree)
instance.gene_KML(filename_KML=filename_kml,col_txt=col_txt,rec_range=rec_range,filename_dire=filename_dire,col_edge_degree=col_edge_degree)