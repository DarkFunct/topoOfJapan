#-*- coding:utf-8 -*-
from second_layer.layout import SecondTopo
import pymongo
client = pymongo.MongoClient()
orig_edge = client['itdkall_info']['edge_all']
db_result = client['itdk_level_new']
col_edge = db_result['shankou_edge']
col_point = db_result['shankou_point']
col_point_degree = db_result['shankou_point_degree']
col_edge_degree = db_result['shankou_edge_degree']
col_txt = db_result['shankou_txt']
city_info = {'name':'shankou','longitude':131.463559,'latitude':34.178906,'range':30,'degree':0}
instance = SecondTopo()
filename_txt='./file/shankou_edge.txt'
filename_kml='./file/shankou_第二层.kml'
rec_range = {'left':131.347391,'bottom':34.122115 ,'top':34.225061,'right':131.484681}
filename_dire = './file/shankou_dire.txt'
# instance.take_out(col_edge=col_edge,city_info=city_info,edge_collection=orig_edge)
# instance.degree_statistic(col_point=col_point,col_edge=col_edge)
# instance.gt_degree(col_point_degree=col_point_degree,col_point=col_point,degree=city_info['degree'])
# instance.find_link(col_edge_degree=col_edge_degree,col_edge=col_edge,col_point_degree=col_point_degree)
# instance.edge2txt(col_txt=col_txt,filename=filename_txt,col_edge_degree=col_edge_degree)
instance.gene_KML(filename_KML=filename_kml,col_txt=col_txt,rec_range=rec_range,filename_dire=filename_dire,col_edge_degree=col_edge_degree)