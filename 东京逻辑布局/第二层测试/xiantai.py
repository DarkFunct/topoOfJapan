#-*- coding:utf-8 -*-
from second_layer.layout import SecondTopo
import pymongo
client = pymongo.MongoClient()
orig_edge = client['itdkall_info']['edge_all']
db_result = client['itdk_level_new']
col_edge = db_result['xiantai_edge']
col_point = db_result['xiantai_point']
col_point_degree = db_result['xiantai_point_degree']
col_edge_degree = db_result['xiantai_edge_degree']
col_txt = db_result['xiantai_txt']
city_info = {'name':'xiantai','longitude':140.8294,'latitude':38.2361,'range':50,'degree':20}
instance = SecondTopo()
filename_txt='./file/xiantai_edge.txt'
filename_kml='./file/xiantai_第二层.kml'
rec_range = {'left':140.84778950105,'bottom':38.205455683991 ,'top':38.34049333768,'right':140.949686781358}
filename_dire = './file/xiantai_dire.txt'
# instance.take_out(col_edge=col_edge,city_info=city_info,edge_collection=orig_edge)
# instance.degree_statistic(col_point=col_point,col_edge=col_edge)
# instance.gt_degree(col_point_degree=col_point_degree,col_point=col_point,degree=city_info['degree'])
# instance.find_link(col_edge_degree=col_edge_degree,col_edge=col_edge,col_point_degree=col_point_degree)
# instance.edge2txt(col_txt=col_txt,filename=filename_txt,col_edge_degree=col_edge_degree)
instance.gene_KML(filename_KML=filename_kml,col_txt=col_txt,rec_range=rec_range,filename_dire=filename_dire,col_edge_degree=col_edge_degree)