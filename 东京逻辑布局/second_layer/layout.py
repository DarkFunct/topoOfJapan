#-*- coding:utf-8 -*-
'''
布局类，第二层
'''
from math import pi,acos,sin,cos
from Tokyo_logistic_topo.kml_tool import ITDKkml
class SecondTopo:
    def __init__(self):
        pass
    #将一个城市的连接关系取出来
    def take_out(self, col_edge, city_info,edge_collection):
        '''
        :param col_edge: 存储提取出来的边
        :param city_info: 城市信息，eg:{'name':'Nagoya','longitude':136.9064,'latitude':35.1806,'range':60}
            range 代表以此城市为中心的半径长度
        :param edge_collection: 从这个边的集合中提取出边，这里选的是edge_all(所有边，一个ip的也算)
        :return: None
        '''
        col_edge.drop()
        wB = city_info['latitude'] / 180 * pi
        jB = city_info['longitude'] / 180 * pi
        haha_range = city_info['range']
        for edge in edge_collection.find():
            wA = edge['start']['latitude']/180*pi
            jA = edge['start']['longitude']/180*pi
            distance = 6371*acos(sin(wA)*sin(wB)+cos(wA)*cos(wB)*cos(jA-jB))
            if distance<=haha_range:
                wA = edge['end']['latitude']/180*pi
                jA = edge['end']['longitude']/180*pi
                distance = 6371*acos(sin(wA)*sin(wB)+cos(wA)*cos(wB)*cos(jA-jB))
                if distance<=haha_range:
                    col_edge.insert_one(edge)
                    print("insert edge:",edge['_id'])
    #将连接关系中的点的度数统计出来
    def degree_statistic(self,col_point,col_edge):
        '''
        :param col_point: 点的集合，同一地理位置的点视为一个点，统计度数
        :param col_edge: 边的集合，统计边中点的度数
        :return: None
        '''
        #将每个点的度数统计出来存到数据库（出入度都算）,地理位置相同的视为一个点
        col_point.drop()
        for edge in col_edge.find():
            flag = col_point.find_one({'longitude':edge['start']['longitude'], 'latitude':edge['start']['latitude']})
            if flag:
                col_point.update_one({'_id':flag['_id']}, {'$set':{'number': flag['number'] + 1}})
            else:
                col_point.insert_one({'longitude':edge['start']['longitude'], 'latitude':edge['start']['latitude'], 'number':1})
            flag = col_point.find_one({ 'longitude':edge['end']['longitude'], 'latitude':edge['end']['latitude']})
            if flag:
                col_point.update_one({'_id':flag['_id']}, {'$set':{'number': flag['number'] + 1}})
            else:
                col_point.insert_one({ 'longitude':edge['end']['longitude'], 'latitude':edge['end']['latitude'], 'number':1})
            print('processed',edge['_id'])
    #找出度数大于某一值的点
    def gt_degree(self,col_point_degree,col_point,degree):
        '''
        :param col_point_degree: 度数大于某一值的点的集合
        :param col_point: 原始点集合
        :param degree: 度数
        :return: None
        '''
        col_point_degree.drop()
        for node in col_point.find({'number':{'$gt':degree}}):
            col_point_degree.insert({'longitude':node['longitude'], 'latitude':node['latitude']})
        print('the number of point thats degree is greater than',degree,'is:',col_point_degree.count())
    #找出度数比较大的点的连接关系
    def find_link(self,col_edge_degree,col_edge,col_point_degree):
        '''
        :param col_edge_degree: 度数较大的点的连接关系
        :param col_edge: 原始边集合
        :param col_point_degree: 度数较大的点的集合
        :return:
        '''
        col_edge_degree.drop()
        for edge in col_edge.find():
            flag1 = col_point_degree.find_one({'longitude':edge['start']['longitude'], 'latitude':edge['start']['latitude']})
            if flag1:
                flag2 = col_point_degree.find_one({'longitude':edge['end']['longitude'], 'latitude':edge['end']['latitude']})
                if flag2:
                    if not col_edge_degree.find_one({'start':{'longitude':edge['start']['longitude'],'latitude':edge['start']['latitude']},
                        'end':{'longitude':edge['end']['longitude'], 'latitude':edge['end']['latitude']}}) and edge['start']['longitude']!=edge['end']['longitude']\
                            and edge['start']['latitude']!=edge['end']['latitude']:
                        col_edge_degree.insert_one({'start':{'longitude':edge['start']['longitude'],'latitude':edge['start']['latitude']},'end':{'longitude':edge['end']['longitude'], 'latitude':edge['end']['latitude']}})
                        print(edge['_id'])
    #将度数比较大的边的连接关系输出到txt文件
    def edge2txt(self, col_txt, filename, col_edge_degree):
        '''
        :param col_txt: 存储点
        :param filename: 文件名
        :param col_edge_degree:边
        :return: None
        '''
        col_txt.drop()
        node_id_1 = ''
        node_id_2 = ''
        i=1#节点编号从1开始
        f = open(filename, 'w')
        for edge in col_edge_degree.find():
            flag_start = col_txt.find_one({'latitude':edge['start']['latitude'],'longitude':edge['start']['longitude']})
            if flag_start:
                node_id_1 = str(flag_start['node_id'])
            else:
                col_txt.insert({'latitude':edge['start']['latitude'],'longitude':edge['start']['longitude'],'node_id':i})
                node_id_1 = str(i)
                i=i+1
            flag_end = col_txt.find_one({'latitude':edge['end']['latitude'],'longitude':edge['end']['longitude']})
            if flag_end:
                node_id_2 = str(flag_end['node_id'])
            else:
                col_txt.insert({'latitude':edge['end']['latitude'],'longitude':edge['end']['longitude'],'node_id':i})
                node_id_2 = str(i)
                i=i+1
            s = node_id_1+' '+node_id_2+'\n'
            f.write(s)
        f.close()
        node_num = col_txt.count()
        edge_num = col_edge_degree.count()
        with open(filename, 'r+') as f:
            old = f.read()
            new = 'N:'+str(node_num)+' '+'E:'+str(edge_num)+'\n'
            f.seek(0)
            f.write(new)
            f.write(old)
        print('done')
    #将力导引数据生成KML
    def gene_KML(self,filename_KML,col_txt,rec_range,filename_dire,col_edge_degree):
        node_list = []
        node_num = 0
        with open(filename_dire,'r')as f:
            content = f.readline()
            node_num = int(content.split(' ')[0].split(':')[1])
            print (node_num)
            num=node_num
            content = f.readline()
            while(content and node_num>0):
                ss = content.replace('\n','').split(' ')
                node_list.append(ss)
                content = f.readline()
                node_num=node_num-1
        point_longitude = 0.0
        max_longitude = float(node_list[0][1])
        min_longitude =float( node_list[0][1])
        max_latitude = float(node_list[0][2])
        min_latitude = float(node_list[0][2])
        for i in node_list:
            if float(i[1])<min_longitude:
                min_longitude =float(i[1])
            if float(i[1])>max_longitude:
                max_longitude = float(i[1])
            if float(i[2])<min_latitude:
                min_latitude = float(i[2])
            if float(i[2])>max_latitude:
                max_latitude = float(i[2])
        point_longitude = (max_longitude+min_longitude)/2
        point_latitude = (max_latitude+min_latitude)/2
        orignal_breath_longitude = rec_range['right']-rec_range['left']
        orignal_breath_latitude = rec_range['top']-rec_range['bottom']
        longitude_percent = (max_longitude-min_longitude)/orignal_breath_longitude
        latitude_percent = (max_latitude-min_latitude)/orignal_breath_latitude
        bias_longitude = (rec_range['right']+rec_range['left'])/2-point_longitude
        bias_latitude = (rec_range['top']+rec_range['bottom'])/2-point_latitude
        for node in node_list:
            longitude = (float(node[1])-point_longitude)/longitude_percent+point_longitude
            latitude = (float(node[2])-point_latitude)/latitude_percent+point_latitude
            col_txt.update_one({'node_id':int(node[0])},{'$set':{'new':{'longitude':longitude+bias_longitude,'latitude':latitude+bias_latitude}}})
        #生成KML
        f=open(filename_KML,'w')
        paint = ITDKkml(f)
        paint.setting_line(line_color= 'ffb40014',line_hight_start=80000,line_hight_end=80000,altitudeMode='relativeToGround',line_width=3)
        paint.setting_point(icon_path='juanjo_Router.png',point_hight=80000,point_scale=0.5)
        paint.head()
        for edge in col_edge_degree.find():
             start_new = col_txt.find_one({'longitude':edge['start']['longitude'],'latitude':edge['start']['latitude']})
             end_new = col_txt.find_one({'longitude':edge['end']['longitude'],'latitude':edge['end']['latitude']})
             paint.draw_edge(start=start_new['new'],end=end_new['new'])
        for node in col_txt.find():
            paint.draw_point2(longitude=node['new']['longitude'],latitude=node['new']['latitude'])
        paint.tail()
        f.close()