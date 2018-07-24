#-*- coding:utf-8 -*-
import pymongo
import re,random
from math import pi,acos,sin,cos
from queue import Queue
#以point为根生成树，将边插入到colll里
def gene_tree(point,colll):
    q = Queue()
    hight = random.randint(3,5)#树的高度
    tem = {'point':point,'depth':0,'degree':random.randint(0,360),'lenth':1.0}
    q.put(tem)
    while not q.empty():
        q_get = q.get()
        if q_get['depth']<hight:
            col_point.insert_one(q_get['point'])
            num_sub = random.randint(2,3)#每个节点的度数
            i = 0
            depth = q_get['depth']+1
            while i<num_sub:
                #llll = random.randint(300,600)/1000#边的长度
                llll = q_get['lenth']*0.76
                dududud = q_get['degree']/180*pi
                longitude = (q_get['point']['longitude']+llll*1.5*cos(dududud)/\
                                    111*cos(q_get['point']['latitude']/180*pi))
                latitude = (q_get['point']['latitude']+sin(dududud)/111/1.5)
                tem = {'point':{'longitude':longitude,'latitude':latitude},'depth':depth,
                       'degree':random.randint(q_get['degree']-90,q_get['degree']+90),'lenth':llll}
                if q_get['depth']<hight-1:
                    colll.insert_one({'start':q_get['point'],'end':tem['point']})
                else:
                    col_edge_leaf.insert_one({'start':q_get['point'],'end':tem['point']})
                q.put(tem)
                i+=1
        else:
            col_point_leaf.insert_one(q_get['point'])
def get_distance(start,end):
    wB = start['latitude']/180*pi
    jB = start['longitude']/180*pi
    wA = end['latitude']/180*pi
    jA = end['longitude']/180*pi
    distance = 6371*acos(sin(wA)*sin(wB)+cos(wA)*cos(wB)*cos(jA-jB))
    return distance
client = pymongo.MongoClient()
col=client['教育科研网']['图中点']
col_300 = client['教育科研网']['300大学']
col_edge = client['教育科研网']['大学边']
col_edge_leaf = client['教育科研网']['叶子边']
col_edge_leaf.drop()
col_point = client['教育科研网']['大学里面的点']
col_point.drop()
col_edge.drop()
col_point_leaf = client['教育科研网']['叶子节点']
col_point_leaf.drop()
for node in col_300.find():
    min = {}
    min_len = 10000
    for po in col.find():
        lenth = get_distance(start=node,end=po)
        if lenth<min_len:
            min_len=lenth
            min={'longitude':po['longitude'],'latitude':po['latitude']}
    docu = {'start':{'longitude':node['longitude'],'latitude':node['latitude']},
            'end':min}
    col_edge.insert_one(docu)
ooo=0
for node in col_300.find():
    print(node,ooo)
    ooo+=1
    iii = {'longitude':node['longitude'],'latitude':node['latitude']}
    gene_tree(point=iii,colll=col_edge)