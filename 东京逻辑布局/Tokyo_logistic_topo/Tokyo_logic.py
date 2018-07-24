#-*- coding:utf-8 -*-
'''
东京逻辑布局的类
'''
from Tokyo_logistic_topo.kml_tool import ITDKkml
from math import pi,acos,sin,cos
from queue import Queue
import random
class TokyoTopo:
    def __init__(self):
        pass
    #从日本的点边关系中提取出东京的
    def extract_tokyo(self,col_Tokyo_edge,col_Tokyo_node,city,col_orignal_edge):
        col_Tokyo_edge.drop()
        col_Tokyo_node.drop()
        col_Tokyo_node.create_index([('node_id', 1)],unique=True)
        point_id = 0
        for edge in col_orignal_edge.find({},{'_id':0},no_cursor_timeout = True):
            flag_start = False
            flag_end = False
            #起点是否在东京
            if edge['start']['longitude']>city['left'] and edge['start']['longitude']<city['right']:
                if edge['start']['latitude']>city['bottom'] and edge['start']['latitude']<city['top']:
                    flag_start = True
            #终点是否在东京
            if edge['end']['longitude']>city['left'] and edge['end']['longitude']<city['right']:
                if edge['end']['latitude']>city['bottom'] and edge['end']['latitude']<city['top']:
                    flag_end = True
            if flag_start and flag_end:
                docu_find = col_Tokyo_node.find_one({'node_id':edge['start']['node_id']})
                if docu_find:
                    node_list = docu_find['adjoin_node']
                    node_list.append(edge['end']['node_id'])
                    col_Tokyo_node.update_one({'_id':docu_find['_id']},{'$set':{'count':docu_find['count']+1,'adjoin_node':node_list}})
                else:
                    docu = {'node_id':edge['start']['node_id'],'count':1,'point_id':point_id,'adjoin_node':[],'connect_flag':False}
                    point_id = point_id + 1
                    col_Tokyo_node.insert_one(docu)
                docu_find = col_Tokyo_node.find_one({'node_id':edge['end']['node_id']})
                if docu_find:
                    node_list = docu_find['adjoin_node']
                    node_list.append(edge['start']['node_id'])
                    col_Tokyo_node.update_one({'_id':docu_find['_id']},{'$set':{'count':docu_find['count']+1,'adjoin_node':node_list}})
                else:
                    docu = {'node_id':edge['end']['node_id'],'count':1,'point_id':point_id,'adjoin_node':[],'connect_flag':False}
                    point_id = point_id + 1
                    col_Tokyo_node.insert_one(docu)
                docu_edge = {'start':edge['start'],'end':edge['end']}
                col_Tokyo_edge.insert_one(docu_edge)
                print('point num:',point_id)
    #将东京的连接关系生成树,并将树的数据输出到txt文件
    def tokyo2tree(self,col_Tokyo_node,col_Tokyo_tree,col_Tokyo_tree_node,col_map,file='tree_data.txt'):
        for node in col_Tokyo_node.find({'connect_flag':True}):
            col_Tokyo_node.update_one({'node_id':node['node_id']},{'$set':{'connect_flag':False}})
        col_Tokyo_tree.drop()
        col_Tokyo_tree_node.drop()
        q=Queue()
        for node in col_Tokyo_node.find():
            q.put(node['node_id'])
            node_number = 1
            while not q.empty():
                node={}
                current_node = q.get()
                node['node_id'] = current_node
                node['connect'] = []
                docu_start = col_Tokyo_node.find_one({'node_id':current_node})
                col_Tokyo_node.update_one({'node_id':current_node},{'$set':{'connect_flag':True}})
                for node_id in docu_start['adjoin_node']:
                    docu_end = col_Tokyo_node.find_one({'node_id':node_id})
                    #如果没有连接过，进行连接，置标志位为1,如果被连接过，说明已经在队列里面了
                    if not docu_end['connect_flag']:
                        node['connect'].append(node_id)
                        col_Tokyo_tree.insert_one({'start':current_node,'end':node_id})
                        col_Tokyo_node.update_one({'node_id':node_id},{'$set':{'connect_flag':True}})
                        q.put(node_id)
                        print(current_node,node_id)
                col_Tokyo_tree_node.insert_one(node)
                node_number = node_number+1
            if node_number<70:
                col_Tokyo_tree.drop()
                col_Tokyo_tree_node.drop()
            else:
                break
        m = col_Tokyo_tree.count()
        n = m+1
        col_map.drop()
        col_map.create_index([('node_id', 1)], unique=True)
        with open(file,'w') as f:
            content = 'N:'+str(n)+' E:'+str(m)+'\n'
            f.write(content)
            node_id1 = ''
            node_id2 = ''
            i=1
            for edge in col_Tokyo_tree.find():
                flag_start = col_map.find_one({'node_id':edge['start']})
                if flag_start:
                    node_id1 = str(flag_start['point_id'])
                else:
                    col_map.insert_one({'node_id':edge['start'], 'point_id':i})
                    node_id1 =str(i)
                    i = i+1
                flag_end = col_map.find_one({'node_id':edge['end']})
                if flag_end:
                    node_id2 = str(flag_end['point_id'])
                else:
                    col_map.insert_one({'node_id':edge['end'], 'point_id':i})
                    node_id2 =str(i)
                    i = i+1
                content = node_id1+' '+node_id2+'\n'
                f.write(content)
    #将坐标转化为日本的
    def coor2japan(self,city,col_map,txt_name='PajekData.txt'):
        node_list = []
        node_num = 0
        with open(txt_name,'r')as f:
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
        orignal_breath_longitude = city['right']-city['left']
        orignal_breath_latitude = city['top']-city['bottom']
        longitude_percent = (max_longitude-min_longitude)/orignal_breath_longitude
        latitude_percent = (max_latitude-min_latitude)/orignal_breath_latitude
        bias_longitude = (city['right']+city['left'])/2-point_longitude
        bias_latitude = (city['top']+city['bottom'])/2-point_latitude
        for node in node_list:
            longitude = (float(node[1])-point_longitude)/longitude_percent+point_longitude
            latitude = (float(node[2])-point_latitude)/latitude_percent+point_latitude
            col_map.update_one({'point_id':int(node[0])},{'$set':{'new':{'longitude':longitude+bias_longitude,'latitude':latitude+bias_latitude}}})
    #1.将叶子节点散射为星状，毛茸茸，说是不像拓扑，不用
    def leaf2star(self,col_Tokyo_tree_node,col_Tokyo_tree,col_map,col_parent):
        col_parent.drop()
        col_parent.create_index([('node_id', 1)],unique=True)
        for node in col_Tokyo_tree_node.find({'connect':[]}):#叶子节点
            parent_node = col_Tokyo_tree.find_one({'end':node['node_id']})
            flag = col_parent.find_one({'node_id':parent_node['start']})
            if not flag:
                col_parent.insert_one({'node_id':parent_node['start'],'connect_child':[node['node_id']]})
            else:
                print(flag['connect_child'])
                child_list = flag['connect_child']
                child_list.append(node['node_id'])
                print(child_list)
                col_parent.update_one({'node_id':parent_node['start']},{'$set':{'connect_child':child_list}})
        for node in col_parent.find():
            parent_location = col_map.find_one({'node_id':node['node_id']})
            child_location = col_map.find_one({'node_id':node['connect_child'][0]})
            min_distance = self.__get_distance(parent_location['new'],child_location['new'])
            for connect_node in node['connect_child']:
                child_location = col_map.find_one({'node_id':connect_node})
                distance = self.__get_distance(parent_location['new'],child_location['new'])
                if distance<min_distance:
                    min_distance=distance
            i=0
            share_one = 2*pi/len(node['connect_child'])
            if len(node['connect_child'])==2:
                for connect_node in node['connect_child']:
                    longitude = parent_location['new']['longitude']+min_distance*cos((i+1)*pi/3)/111*cos(parent_location['new']['latitude']/180*pi)
                    latitude = parent_location['new']['latitude']+min_distance*sin((i+1)*pi/3)/111
                    col_map.update_one({'node_id':connect_node}, {'$set':{'new':{'longitude':longitude, 'latitude':latitude}}})
            else:
                for connect_node in node['connect_child']:
                    longitude = parent_location['new']['longitude']+random.uniform(0.5,1)*min_distance*cos(i*share_one)/111*cos(parent_location['new']['latitude']/180*pi)
                    latitude = parent_location['new']['latitude']+random.uniform(0.5,1)*min_distance*sin(i*share_one)/111
                    col_map.update_one({'node_id':connect_node}, {'$set':{'new':{'longitude':longitude, 'latitude':latitude}}})
                    i=i+1
    #去除范围外的点边关系
    def delete_point_of_polygon(self,polygon,col_map):
        for node in col_map.find():
            col_map.update_one({'node_id':node['node_id']},{'$set':{'in':True}})
        for node in col_map.find():
            if not self.__point_in_polygon(tar_point=node['new'],polygon=polygon):
                col_map.update_one({'node_id':node['node_id']},{'$set':{'in':False}})
    #新树
    def new_tree(self,col_Tokyo_tree_node,col_Tokyo_tree,col_map):
        for node in col_Tokyo_tree_node.find({'connect':[]}):#叶子节点
            parent_node = col_Tokyo_tree.find_one({'end':node['node_id']})
            child_list=col_Tokyo_tree_node.find_one({'node_id':parent_node['start']})['connect']
            child_list.remove(node['node_id'])
            col_Tokyo_tree_node.update_one({'node_id':parent_node['start']},{'$set':{'connect':child_list}})
            col_map.update_one({'node_id':node['node_id']},{'$set':{'in':False}})
    #将处理的最后结果生成KML,有叶子节点
    def geneKML(self,col_Tokyo_tree,col_Tokyo_tree_node,col_map,file_name = r'Tokyo.kmz'):
        fkml=open(file_name,'w')
        paint = ITDKkml(fkml)
        paint.setting_line(line_color='cc00ff00',line_width=0.8)
        paint.setting_point(icon_path='http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png',point_scale=0.4,point_color='ff00ffff')
        paint.head()
        paint.setting_line(line_color='cc0000ff',line_width=1.7)
        paint.setting_point(icon_path='http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png',point_scale=1,point_color='cc0000ff')
        for edge in col_Tokyo_tree.find():
            start_edge = col_map.find_one({'node_id':edge['start']})
            end_edge = col_map.find_one({'node_id':edge['end']})
            if start_edge['in'] and end_edge['in']:
                s = col_Tokyo_tree_node.find_one({'node_id':edge['start']})
                e = col_Tokyo_tree_node.find_one({'node_id':edge['end']})
                #这种方法会使叶子节点父节点多次绘制
                if s['connect']==[] or e['connect']==[]:
                    paint.draw_edge(start=start_edge['new'],end=end_edge['new'])
                else:
                    paint.draw_orig_edge(start=start_edge['new'],end=end_edge['new'])
        for node in col_map.find():
            if node['in']:
                docu = col_Tokyo_tree_node.find_one({'node_id':node['node_id']})
                if len(docu['connect'])<5:
                    paint.draw_point2(longitude=node['new']['longitude'],latitude=node['new']['latitude'])
                else:
                    paint.draw_orig_point(longitude=node['new']['longitude'],latitude=node['new']['latitude'])
        paint.tail()
        fkml.close()
    ##将处理的最后结果生成KML,无叶子节点
    def geneKML_no_leaf(self,col_Tokyo_tree,col_map,col_Tokyo_tree_node,file_name = r'Tokyo.kmz'):
        fkml=open(file_name,'w')
        paint = ITDKkml(fkml)
        paint.setting_line(line_color='cc00ff00',line_width=0.8)
        paint.setting_point(icon_path='http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png',point_scale=0.4,point_color='ff00ffff')
        paint.head()
        paint.setting_line(line_color='cc0000ff',line_width=1.7)
        paint.setting_point(icon_path='http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png',point_scale=1,point_color='cc0000ff')
        for edge in col_Tokyo_tree.find():
            start_edge = col_map.find_one({'node_id':edge['start']})
            end_edge = col_map.find_one({'node_id':edge['end']})
            if start_edge['in'] and end_edge['in']:
                s = col_Tokyo_tree_node.find_one({'node_id':edge['start']})
                e = col_Tokyo_tree_node.find_one({'node_id':edge['end']})
                #这种方法会使叶子节点父节点多次绘制
                if s['connect']==[] or e['connect']==[]:
                    paint.draw_edge(start=start_edge['new'],end=end_edge['new'])
                else:
                    paint.draw_orig_edge(start=start_edge['new'],end=end_edge['new'])
        for node in col_map.find():
            if node['in']:
                docu = col_Tokyo_tree_node.find_one({'node_id':node['node_id']})
                if len(docu['connect'])<5:
                    paint.draw_point2(longitude=node['new']['longitude'],latitude=node['new']['latitude'])
                else:
                    paint.draw_orig_point(longitude=node['new']['longitude'],latitude=node['new']['latitude'])
            pass
        paint.tail()
        fkml.close()

    def get_distance(self,start,end):
        return self.__get_distance(start=start,end=end)
    #地球上两点之间的距离，私有函数
    def __get_distance(self,start,end):
        wB = start['latitude']/180*pi
        jB = start['longitude']/180*pi
        wA = end['latitude']/180*pi
        jA = end['longitude']/180*pi
        distance = 6371*acos(sin(wA)*sin(wB)+cos(wA)*cos(wB)*cos(jA-jB))
        return distance
    #point in polygon
    def __point_in_polygon(self,tar_point,polygon):
        '''
        point in polygon问题，因为是大致范围，所以不要求精确性，不考虑点在多边形边上的复杂情况
        @tar_point:目标点，为一个字典{'longitude';num_l,'latitude':num_2}
        @polygon:目标多边形，为一个列表，[point_1,point_2,...,point_n]
        '''
        flag = False
        i=0
        size = len(polygon)
        while i<size:
            start = i%size
            end = (i+1)%size
            if tar_point['latitude'] < (min(polygon[start]['latitude'],polygon[end]['latitude']))or \
                    tar_point['latitude'] > (max(polygon[start]['latitude'],polygon[end]['latitude'])) or \
                    polygon[start]['latitude'] == polygon[end]['latitude']:
                i = i+1
            else:
                res_longi = (tar_point['latitude']-polygon[start]['latitude'])*\
                            (polygon[end]['longitude']-polygon[start]['longitude'])/\
                            (polygon[end]['latitude']-polygon[start]['latitude'])+polygon[start]['longitude']
                if res_longi>tar_point['longitude']:
                    flag = not flag
                i = i+1
        return flag