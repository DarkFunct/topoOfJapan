#-*- coding:utf-8 -*-
import pymongo
from Tokyo_logistic_topo.kml_tool import ITDKkml
from Tokyo_logistic_topo.Tokyo_logic import TokyoTopo
client = pymongo.MongoClient()
col_edge_degree = client['itdkall_info']['merge']#边
col_point_degree = client['itdkall_info']['point_location_degree']#点
db = client['itdk_level_new']
col_city_txt = ['Tokyo_txt','daban_txt','fugang_txt','mingguwu_txt','beihaidao_txt','jinze_txt','xiantai_txt',
                'gongqi_txt','guangdao_txt','songshan_txt','xinwu_txt','qiutian_txt','jinze_left_txt','changye_txt',
                'fudao_txt','luerdao_txt','chongsheng_txt','gangshan_txt','gaozhi_txt','wuqu_txt','chuyun_txt',
                'shankou_txt','dafen_txt','changqi_txt','dedao_txt','gaosong_txt','yanshou_txt','jinggnag_txt',
                'binsong_txt']
#先将所有的城市转到一个集合中
col_second = db['point_second_layer']
col_second.drop()
flag_label = 1
for city_col in col_city_txt:
    col = db[city_col]
    for point in col.find():
        docu = {'longitude':point['longitude'],'latitude':point['latitude'],'new':point['new'],'flag':flag_label}
        col_second.insert_one(docu)
        print("insert",city_col,point['_id'],flag_label)
    flag_label = flag_label+1
#画图,边
iii=TokyoTopo()
filename_KML = './file/日本整个第二层.kml'
f=open(filename_KML,'w')
paint = ITDKkml(f)
paint.setting_line(line_color= '33ffff00',line_hight_start=40000,altitudeMode='absolute',line_hight_end=40000,line_width=1)
#paint.setting_point(icon_path='juanjo_Router.png',point_hight=80000,point_scale=0.5)
paint.head()

for edge in col_edge_degree.find():
    if iii.get_distance(start=edge['start'],end=edge['end'])<400:
        flag1 = col_second.find_one({'longitude':edge['start']['longitude'], 'latitude':edge['start']['latitude']})
        flag2 = col_second.find_one({'longitude':edge['end']['longitude'], 'latitude':edge['end']['latitude']})
        if flag1 and flag2:
            if flag1['flag']==flag2['flag']:
                pass
            else:
                paint.draw_edge(start=flag1['new'],end=flag2['new'])
        elif flag1 and not flag2:
            paint.draw_edge(start=flag1['new'],end=edge['end'])
        elif not flag1 and flag2:
            paint.draw_edge(start=edge['start'],end=flag2['new'])
        else:
            paint.draw_edge(start=edge['start'],end=edge['end'])
point1={'longitude':127.715229,'latitude':26.290680}
point2={'longitude':130.761069,'latitude':33.521182}
paint.draw_edge(start=point1,end=point2)
point1={'longitude':127.715229,'latitude':26.290680}
point2={'longitude':135.6005387779446,'latitude':34.62006409535766}
paint.draw_edge(start=point1,end=point2)
paint.tail()
f.close()
