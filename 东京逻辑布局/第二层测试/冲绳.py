#-*- coding:utf-8 -*-
from second_layer.layout import SecondTopo
import pymongo
client = pymongo.MongoClient()
orig_edge = client['itdkall_info']['edge_all']
db_result = client['itdk_level_new']
col_edge = db_result['chongsheng_edge']
col_point = db_result['chongsheng_point']
col_point_degree = db_result['chongsheng_point_degree']
col_edge_degree = db_result['chongsheng_edge_degree']
col_txt = db_result['chongsheng_txt']
city_info = {'name':'chongsheng','longitude':127.877791,'latitude': 26.434312,'range':80,'degree':60}
instance = SecondTopo()
filename_txt='./file/chongsheng_edge.txt'
filename_kml='./file/chongsheng_第二层.kml'
rec_range = {'left':127.643642,'bottom':26.271788 ,'top':26.326301,'right':127.850209}
filename_dire = './file/chongsheng_dire.txt'
# instance.take_out(col_edge=col_edge,city_info=city_info,edge_collection=orig_edge)
# instance.degree_statistic(col_point=col_point,col_edge=col_edge)
# instance.gt_degree(col_point_degree=col_point_degree,col_point=col_point,degree=city_info['degree'])
# instance.find_link(col_edge_degree=col_edge_degree,col_edge=col_edge,col_point_degree=col_point_degree)
# instance.edge2txt(col_txt=col_txt,filename=filename_txt,col_edge_degree=col_edge_degree)
instance.gene_KML(filename_KML=filename_kml,col_txt=col_txt,rec_range=rec_range,filename_dire=filename_dire,col_edge_degree=col_edge_degree)