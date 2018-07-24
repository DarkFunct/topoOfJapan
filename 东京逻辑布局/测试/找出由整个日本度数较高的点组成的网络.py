#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.kml_tool import ITDKkml
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
client = pymongo.MongoClient()
col_edge = client['itdkall_info']['edge_all']
col_point = client['itdkall_info']['point_location']#日本所有点的集合
#统计日本每个点的度数
# i=1
#col_point.drop()
# for edge in col_edge.find():
#     flag = col_point.find_one({'longitude':edge['start']['longitude'], 'latitude':edge['start']['latitude']})
#     if flag:
#         col_point.update_one({'_id':flag['_id']}, {'$set':{'number': flag['number'] + 1}})
#     else:
#         col_point.insert_one({'longitude':edge['start']['longitude'], 'latitude':edge['start']['latitude'], 'number':1})
#     flag = col_point.find_one({ 'longitude':edge['end']['longitude'], 'latitude':edge['end']['latitude']})
#     if flag:
#         col_point.update_one({'_id':flag['_id']}, {'$set':{'number': flag['number'] + 1}})
#     else:
#         col_point.insert_one({ 'longitude':edge['end']['longitude'], 'latitude':edge['end']['latitude'], 'number':1})
#     print('processed:',edge['_id'],i)
#     i=i+1
# col_point_degree = client['itdkall_info']['point_location_degree'] #日本度数大于某一值点的集合
# degree = 1000#最原始为2000
# col_point_degree.drop()
# for node in col_point.find({'number':{'$gt':degree}}):
#     col_point_degree.insert({'longitude':node['longitude'], 'latitude':node['latitude']})
# print('the number of point thats degree is greater than',degree,'is:',col_point_degree.count())
#
col_edge_degree = client['itdkall_info']['edge_location_degree_1000'] #日本度数大于某一点的点所组成的边的集合
# col_edge_degree.drop()
# i=1
# for edge in col_edge.find():
#     flag1 = col_point_degree.find_one({'longitude':edge['start']['longitude'], 'latitude':edge['start']['latitude']})
#     if flag1:
#         flag2 = col_point_degree.find_one({'longitude':edge['end']['longitude'], 'latitude':edge['end']['latitude']})
#         if flag2:
#             if not col_edge_degree.find_one({'start':{'longitude':edge['start']['longitude'],'latitude':edge['start']['latitude']},
#                 'end':{'longitude':edge['end']['longitude'], 'latitude':edge['end']['latitude']}}) and edge['start']['longitude']!=edge['end']['longitude']\
#                     and edge['start']['latitude']!=edge['end']['latitude']:
#                 col_edge_degree.insert_one({'start':{'longitude':edge['start']['longitude'],'latitude':edge['start']['latitude']},'end':{'longitude':edge['end']['longitude'], 'latitude':edge['end']['latitude']}})
#                 print(edge['_id'])
#     print(i)
#     i=i+1
#画图
iii=TokyoTopo()
filename_KML = './file/日本整个第二层1000.kml'
f=open(filename_KML,'w')
paint = ITDKkml(f)
paint.setting_line(line_color= 'ffb40014',line_hight_start=0,line_hight_end=0,line_width=1)
#paint.setting_point(icon_path='juanjo_Router.png',point_hight=80000,point_scale=0.5)
paint.head()
for edge in col_edge_degree.find():
    if iii.get_distance(start=edge['start'],end=edge['end'])<400:
        paint.draw_edge(start=edge['start'],end=edge['end'])
paint.tail()
f.close()
