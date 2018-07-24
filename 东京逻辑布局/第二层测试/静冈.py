#-*- coding:utf-8 -*-
from second_layer.layout import SecondTopo
import pymongo
client = pymongo.MongoClient()
orig_edge = client['itdkall_info']['edge_all']
db_result = client['itdk_level_new']
col_edge = db_result['jinggang_edge']
col_point = db_result['jinggang_point']
col_point_degree = db_result['jinggang_point_degree']
col_edge_degree = db_result['jinggang_edge_degree']
col_txt = db_result['jinggang_txt']
city_info = {'name':'jinggang','longitude':138.419814,'latitude': 34.984957,'range':17,'degree':1}
instance = SecondTopo()
filename_txt='./file/jinggang_edge.txt'
filename_kml='./file/jinggang_第二层.kml'
rec_range = {'left':138.313450,'bottom': 34.941465,'top':35.034162,'right':138.522456}
filename_dire = './file/jinggang_dire.txt'
# instance.take_out(col_edge=col_edge,city_info=city_info,edge_collection=orig_edge)
# instance.degree_statistic(col_point=col_point,col_edge=col_edge)
# instance.gt_degree(col_point_degree=col_point_degree,col_point=col_point,degree=city_info['degree'])
# instance.find_link(col_edge_degree=col_edge_degree,col_edge=col_edge,col_point_degree=col_point_degree)
# instance.edge2txt(col_txt=col_txt,filename=filename_txt,col_edge_degree=col_edge_degree)
instance.gene_KML(filename_KML=filename_kml,col_txt=col_txt,rec_range=rec_range,filename_dire=filename_dire,col_edge_degree=col_edge_degree)