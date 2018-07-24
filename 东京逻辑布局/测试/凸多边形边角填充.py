#-*- coding:utf-8 -*-
from Tokyo_logistic_topo.kml_tool import ITDKkml
from math import pi,acos,sin,cos
def get_distance(start,end):
        wB = start['latitude']/180*pi
        jB = start['longitude']/180*pi
        wA = end['latitude']/180*pi
        jA = end['longitude']/180*pi
        distance = 6371*acos(sin(wA)*sin(wB)+cos(wA)*cos(wB)*cos(jA-jB))
        return distance
polygon = [{'longitude':-1,'latitude':0},
           {'longitude':3,'latitude':0},
           {'longitude':1.5,'latitude':2}]
edge=[[1,4],[2,4],[3,4],[4,6],[5,6],[6,7],[6,8],[7,9],[7,10],[10,11]]
point_original = [[0.2,0.7],[0.5,1],[0.7,0.2],[0.8,0.6],[1.3,0.3],[1.4,0.9],[1.1,1.1],[1.6,0.4],[1.7,0.7],[1.6,1.2],[2,1.1]]
#原始位置图
file_name = 'original.kml'
fkml=open(file_name,'w')
paint = ITDKkml(fkml)
paint.setting_line(line_color='cc00ff00',line_width=0.8)
paint.setting_point(icon_path='http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png',point_scale=0.4,point_color='ff00ffff')
paint.head()
polygon_point_num = len(polygon)
i=0
while i<polygon_point_num-1:
    paint.draw_edge(start=polygon[i],end=polygon[i+1])
    i=i+1
paint.draw_edge(start=polygon[polygon_point_num-1],end=polygon[0])
for node in point_original:
    paint.draw_orig_point(longitude=node[0],latitude=node[1])
for e in edge:
    paint.draw_edge(start={'longitude':point_original[e[0]-1][0],'latitude':point_original[e[0]-1][1]},\
                    end={'longitude':point_original[e[1]-1][0],'latitude':point_original[e[1]-1][1]})
paint.tail()
fkml.close()
#开始处理
point_new=[[0.2,0.7],[0.5,1],[0.7,0.2],[0.8,0.6],[1.3,0.3],[1.4,0.9],[1.1,1.1],[1.6,0.4],[1.7,0.7],[1.6,1.2],[2,1.1]]
center_x=0
center_y=0
i=0
for node in point_original:
    center_x=center_x+node[0]
    center_y=center_y+node[1]
    i=1+i
center_x=center_x/i
center_y=center_y/i
for pole_node in polygon:
    radias  = get_distance(start=pole_node,end={'longitude':center_x,'latitude':center_y})
    R_min = radias
    new_pole_p_ori = {}
    point_process_index=[]#待位移的点，用下标表示
    i=0
    for node in point_original:
        now_r = get_distance(start=pole_node,end={'longitude':node[0],'latitude':node[1]})
        if now_r<radias:
            point_process_index.append(i)
            point_new[i]=[point_new[i][0]-pole_node['longitude'],point_new[i][1]-pole_node['latitude']]
            new_pole_p_ori[i] = now_r
            if now_r<R_min:
                R_min=now_r
        i=i+1
    for items in point_process_index:
        p = radias-(radias-new_pole_p_ori[items])/(radias-R_min)*0.9*radias
        x = point_new[items][0]*p/new_pole_p_ori[items]
        y = point_new[items][1]*p/new_pole_p_ori[items]
        point_new[items]=[x+pole_node['longitude'],y+pole_node['latitude']]
#处理之后
file_name = 'processed.kml'
fkml=open(file_name,'w')
paint = ITDKkml(fkml)
paint.setting_line(line_color='cc0000ff',line_width=1.7)
paint.setting_point(icon_path='http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png',point_scale=1,point_color='cc0000ff')
paint.head()
polygon_point_num = len(polygon)
i=0
while i<polygon_point_num-1:
    paint.draw_edge(start=polygon[i],end=polygon[i+1])
    i=i+1
paint.draw_edge(start=polygon[polygon_point_num-1],end=polygon[0])
for node in point_new:
    paint.draw_orig_point(longitude=node[0],latitude=node[1])
for e in edge:
    paint.draw_edge(start={'longitude':point_new[e[0]-1][0],'latitude':point_new[e[0]-1][1]},\
                    end={'longitude':point_new[e[1]-1][0],'latitude':point_new[e[1]-1][1]})
paint.tail()
fkml.close()

