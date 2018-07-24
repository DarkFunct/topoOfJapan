#-*- coding:utf-8 -*-
from Tokyo_logistic_topo.kml_tool import ITDKkml
polygon_list = []
with open('坐标.txt','r') as f:
    edge_list = []
    content=f.readline()
    while content:
        if content == '\n':
            polygon_list.append(edge_list)
            edge_list = []
        else:
            coor = content.replace('\n','').split('\t')
            print(coor)
            point  = {'longitude':coor[1],'latitude':coor[0]}
            edge_list.append(point)
        content = f.readline()
    polygon_list.append(edge_list)
print(polygon_list[0])
f=open('polygon.kml','w')
instance = ITDKkml(f)
instance.setting_line(line_color='641400FF',line_width=4)
instance.head()
for polygon in polygon_list:
    lenth = len(polygon)
    i = 0
    while i<(lenth-1):
        instance.draw_edge(start=polygon[i],end=polygon[i+1])
        i = i+1
    instance.draw_edge(start=polygon[-1],end=polygon[0])
instance.tail()