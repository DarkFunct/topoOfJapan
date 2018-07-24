#-*- coding:utf-8 -*-
from Tokyo_logistic_topo.kml_tool import ITDKkml
point={'电子科大':[104.0667,30.6667],'浙大':[120.1614,30.2936],'上海交大':[121.42509,31.022],'北邮':[116.3517916,39.959013],
       '北航':[116.340848,39.97924],'北大':[116.3044,39.9923],'清华':[116.3263,40.003834],'中山':[113.25,23.1167],
       '重庆邮电':[106.5528,29.5628],'华中科大':[114.2734,30.5801],'中科大':[117.2808,31.8639]}
point_edge = [[104.058986,30.676235],[120.161519,30.295558],[121.468973,31.232382],[116.391464,39.903152],
              [116.391464,39.903152],[116.391464,39.903152],[116.391464,39.903152],[113.295827,23.116548],
              [106.547819,29.565937],[114.304197,30.577806],[117.270667,31.863063]]
filename_KML = './教育科研网_测量点.kml'
f=open(filename_KML,'w')
paint = ITDKkml(f)
#paint.setting_line(line_hight_start=40000,line_hight_end=40000,line_width=5)
#paint.setting_point(icon_path='juanjo_Router.png',point_hight=80000,point_scale=0.5)
paint.head()
i=0
for node in point:
    print(point[node])
    paint.draw_orig_point(longitude=point[node][0],latitude=point[node][1])
    paint.draw_edge(start={'longitude':point[node][0],'latitude':point[node][1]},
                    end={'longitude':point_edge[i][0],'latitude':point_edge[i][1]})
    i+=1
paint.tail()
f.close()
